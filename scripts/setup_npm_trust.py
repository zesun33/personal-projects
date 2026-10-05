#!/usr/bin/env python3
"""Plan, check, or create npm trust for the catalog's published packages."""
import argparse
import base64
import json
import os
import re
import shlex
import subprocess
import sys
import time

from catalog import ROOT, load_catalog, normalize_git_url

REGISTRY = 'https://registry.npmjs.org'
WORKFLOW = 'publish.yml'


def command(args, interactive=False):
    result = subprocess.run(args, cwd=ROOT, text=True,
                            capture_output=not interactive,
                            env={**os.environ, 'NO_COLOR': '1', 'npm_config_color': 'false'})
    if result.returncode:
        # npm's captured output can contain authentication URLs. Show npm errors,
        # but leave passwords, tokens, and OTPs entirely in the browser flow.
        raise RuntimeError('Command failed: ' + shlex.join(args) +
                           ('\n' + result.stderr.strip() if not interactive else ''))
    return result.stdout or ''


def targets(root=ROOT, selected=None):
    projects = [p for p in load_catalog(root)['projects'] if p.get('npm_published')]
    if selected:
        unknown = set(selected) - {p['path'] for p in projects}
        if unknown:
            raise ValueError('Not published npm projects: ' + ', '.join(sorted(unknown)))
        projects = [p for p in projects if p['path'] in selected]
    for p in projects:
        directory = root / p['path']
        package = json.loads((directory / 'package.json').read_text())
        repository = package['repository']
        repository = repository['url'] if isinstance(repository, dict) else repository
        if package['name'] != p['npm_package'] or normalize_git_url(repository) != p['github']:
            raise ValueError(p['path'] + ': catalog/package repository mismatch')
        if not (directory / '.github/workflows' / WORKFLOW).is_file():
            raise ValueError(p['path'] + ': missing release workflow')
    return projects


def create_args(project):
    return ['npm', 'trust', 'github', project['npm_package'], '--repository',
            project['github'].removeprefix('https://github.com/'), '--file', WORKFLOW,
            '--allow-publish', '--yes', '--browser=false', '--registry=' + REGISTRY]


def parse_configs(output):
    # npm prints a separate JSON object for each configuration, and nothing for
    # an empty list. Decode each complete object rather than parsing log text.
    decoder = json.JSONDecoder()
    remaining = output.strip()
    configs = []
    while remaining:
        value, end = decoder.raw_decode(remaining)
        configs.extend(value if isinstance(value, list) else [value])
        remaining = remaining[end:].strip()
    if any(not isinstance(c, dict) for c in configs):
        raise ValueError('Unexpected npm trust response')
    return configs


def matches(config, project):
    # npm also grants staging permission to direct publishers. Require direct
    # publishing while allowing that server-added permission only.
    permissions = config.get('permissions', [])
    return (config.get('type') == 'github' and
            config.get('repository') == project['github'].removeprefix('https://github.com/') and
            config.get('file') == WORKFLOW and not config.get('environment') and
            isinstance(permissions, list) and 'createPackage' in permissions and
            set(permissions) <= {'createPackage', 'createStagedPackage'})


def list_configs(project):
    output = command(['npm', 'trust', 'list', project['npm_package'], '--json',
                      '--browser=false', '--registry=' + REGISTRY])
    time.sleep(2)
    return parse_configs(output)


def inspect(projects):
    missing = []
    for p in projects:
        configs = list_configs(p)
        if not configs:
            print(p['npm_package'] + ': MISSING', flush=True)
            missing.append(p)
        elif len(configs) == 1 and matches(configs[0], p):
            print(p['npm_package'] + ': VERIFIED', flush=True)
        else:
            raise ValueError(p['npm_package'] + ': existing trust differs; inspect it manually. '
                             'No existing configuration was changed.')
    return missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true', help='Create missing trust configurations')
    mode.add_argument('--check', action='store_true', help='Read and verify npm settings only')
    parser.add_argument('--project', action='append', help='Select one or more catalog project paths')
    args = parser.parse_args()
    projects = targets(selected=args.project)
    if not projects:
        raise ValueError('No published packages selected')
    for p in projects:
        print(shlex.join(create_args(p)), flush=True)
    if not args.apply and not args.check:
        print(f'PLAN: {len(projects)} packages. No network requests or account changes.')
        return 0

    version = command(['npm', '--version']).strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version) or tuple(map(int, version.split('.'))) < (11, 15, 0):
        raise ValueError('npm 11.15.0 or newer is required')
    if args.apply:
        # Establish that every workflow is already on GitHub before granting
        # any publisher. A missing/drifted workflow stops the entire batch.
        for p in projects:
            repository = p['github'].removeprefix('https://github.com/')
            remote = json.loads(command(['gh', 'api',
                f'repos/{repository}/contents/.github/workflows/{WORKFLOW}?ref=main']))
            local = (ROOT / p['path'] / '.github/workflows' / WORKFLOW).read_bytes()
            if base64.b64decode(remote['content']) != local:
                raise ValueError(p['path'] + ': GitHub workflow differs from this checkout')

    user = command(['npm', 'whoami', '--registry=' + REGISTRY]).strip()
    if user != 'zesun33':
        raise ValueError('Sign in to npm as zesun33 before running this batch')
    print('Approve the browser verification and select the option to skip further 2FA '
          'for five minutes. Keep this terminal open.', flush=True)
    # JSON mode buffers the browser URL, so deliberately use human-readable
    # output for the first authentication request, with the terminal inherited.
    command(['npm', 'trust', 'list', projects[0]['npm_package'], '--browser=false',
             '--registry=' + REGISTRY], interactive=True)
    time.sleep(2)
    missing = inspect(projects)
    if not args.apply:
        return int(bool(missing))
    for p in missing:
        command(create_args(p), interactive=True)
        time.sleep(2)
        configs = list_configs(p)
        if len(configs) != 1 or not matches(configs[0], p):
            raise ValueError(p['npm_package'] + ': creation could not be verified')
        print(p['npm_package'] + ': CREATED AND VERIFIED', flush=True)
    print(f'PASS: all {len(projects)} trusted publishers verified. No packages published.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError, RuntimeError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        print('Account setup is incomplete. Fix the error and rerun; matching existing '
              'settings are preserved. Browser verification cannot be unattended.', file=sys.stderr)
        sys.exit(1)

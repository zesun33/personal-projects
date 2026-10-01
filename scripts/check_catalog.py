#!/usr/bin/env python3
"""Validate generated catalog files and optional local/GitHub/npm connections."""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from catalog import ROOT, load_catalog, normalize_git_url
from generate_catalog import outputs


def run(args, cwd=ROOT):
    try:
        result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ValueError(f'{args[0]} failed: {error}') from error
    if result.returncode:
        raise ValueError(result.stderr.strip() or result.stdout.strip() or f'{args[0]} exited {result.returncode}')
    return result.stdout.strip()


def check(root=ROOT, catalog_only=False, network=False):
    data = load_catalog(root)
    errors, notes = [], []
    for name, content in outputs(root).items():
        path = root / name
        if not path.exists() or path.read_text() != content:
            errors.append(f'{name}: generated file drift; run scripts/generate_catalog.py')
    projects = data['projects']
    names = {p['path'] for p in projects}
    local_repos = {p.name for p in root.iterdir() if p.is_dir() and (p / '.git').exists()}
    if local_repos - names:
        errors.append('Uncataloged child repositories: ' + ', '.join(sorted(local_repos - names)))
    for project in projects:
        name = project['path']
        checkout = root / name
        if not checkout.is_dir():
            if not catalog_only:
                errors.append(f'{name}: missing checkout; use scripts/sync_projects.py --clone-missing')
            continue
        if catalog_only:
            continue
        try:
            if not (checkout / 'README.md').is_file():
                raise ValueError('missing README.md')
            if project['github']:
                if not (checkout / '.git').exists():
                    raise ValueError('expected an independent Git repository')
                origin = run(['git', 'remote', 'get-url', 'origin'], checkout)
                if normalize_git_url(origin) != project['github']:
                    raise ValueError(f'origin {origin} != {project["github"]}')
                if run(['git', 'branch', '--show-current'], checkout) != 'main':
                    raise ValueError('current branch is not main')
                ignored = run(['git', 'check-ignore', name], root)
                if ignored != name:
                    raise ValueError('child checkout is not ignored by parent')
                if run(['git', 'status', '--porcelain'], checkout):
                    notes.append(f'{name}: uncommitted changes (not yet on GitHub)')
                if network:
                    local = run(['git', 'rev-parse', 'HEAD'], checkout)
                    remote = run(['git', 'ls-remote', 'origin', 'refs/heads/main'], checkout)
                    if not remote or remote.split()[0] != local:
                        raise ValueError('local HEAD differs from live GitHub main')
            elif (checkout / '.git').exists():
                raise ValueError('metadata track unexpectedly has a separate Git repository')
            for step in project.get('verify_steps', []):
                if step[0].startswith('./'):
                    executable = checkout / step[0]
                    # Build products are made by earlier steps, not committed executables.
                    if not executable.exists() and step[0].startswith('./build/'):
                        continue
                    if not executable.is_file() or not os.access(executable, os.X_OK):
                        raise ValueError(f'missing executable: {step[0]}')
            if not project.get('npm_package'):
                continue
            package = json.loads((checkout / 'package.json').read_text())
            if package.get('name') != project['npm_package']:
                raise ValueError('npm package name does not match catalog')
            repository = package.get('repository', {})
            url = repository.get('url', '') if isinstance(repository, dict) else repository
            if normalize_git_url(url) != project['github']:
                raise ValueError('package repository URL does not match GitHub')
            if not project['npm_published'] and not package.get('private'):
                raise ValueError('source-only package must be marked private')
            lock_path = checkout / 'package-lock.json'
            if lock_path.exists():
                lock = json.loads(lock_path.read_text())
                for entry in [lock, lock['packages']['']]:
                    if (entry.get('name'), entry.get('version')) != (package['name'], package['version']):
                        raise ValueError('package-lock root identity differs from package.json')
                for key in ['dependencies', 'devDependencies']:
                    if lock['packages'][''].get(key, {}) != package.get(key, {}):
                        raise ValueError(f'lockfile {key} differs from package.json')
            if network and project['npm_published']:
                published = json.loads(run(['npm', 'view', package['name'], '--json'], checkout))
                if published['version'] != package['version']:
                    raise ValueError(f'npm latest {published["version"]} != local {package["version"]}')
                normalize_bins = lambda bins: {k: v.removeprefix('./') for k, v in bins.items()}
                if normalize_bins(published.get('bin', {})) != normalize_bins(package.get('bin', {})):
                    raise ValueError('published npm executable mappings differ')
                if normalize_git_url(published.get('repository', {}).get('url', '')) != project['github']:
                    raise ValueError('published npm repository URL differs')
        except (ValueError, KeyError, OSError) as error:
            errors.append(f'{name}: {error}')
    scaffold = root / 'hw-agent-scaffold/template/.cursor/mcp.json'
    if not catalog_only and scaffold.exists():
        servers = json.loads(scaffold.read_text())['mcpServers']
        expected = {p['npm_package'] for p in projects if p['kind'] == 'mcp'}
        actual = {cfg['args'][1] for cfg in servers.values()}
        if actual != expected or len(servers) != len(expected):
            errors.append('Scaffold MCP package list differs from catalog')
        if any(cfg['command'] != 'npx' or cfg['args'][0] != '-y' for cfg in servers.values()):
            errors.append('Scaffold MCP commands must use npx -y')
    return errors, notes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog-only', action='store_true', help='validate metadata without requiring child clones (CI/fresh checkout)')
    parser.add_argument('--network', action='store_true', help='also check live GitHub main and npm registry metadata')
    args = parser.parse_args()
    if args.catalog_only and args.network:
        parser.error('--network requires local checkouts')
    errors, notes = check(catalog_only=args.catalog_only, network=args.network)
    for note in notes:
        print('NOTE:', note)
    for error in errors:
        print('FAIL:', error)
    print('CATALOG CHECK:', 'FAIL' if errors else 'PASS')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())

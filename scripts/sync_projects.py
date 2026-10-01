#!/usr/bin/env python3
"""Clone missing child repositories or update clean main branches with fast-forward pulls."""
import argparse
import subprocess
import sys
from catalog import ROOT, FAMILIES, load_catalog, normalize_git_url


def git(args, cwd):
    result = subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True, timeout=120)
    if result.returncode:
        raise ValueError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def sync(project, root=ROOT, pull=False, clone_missing=False, dry_run=False):
    path = root / project['path']
    url = project['github']
    if not url:
        return 'META (updated with parent catalog)'
    if path.is_symlink():
        raise ValueError('checkout path is a symlink; inspect it manually')
    if not path.exists():
        if not clone_missing:
            return 'MISSING (add --clone-missing)'
        if dry_run:
            return 'WOULD CLONE ' + url
        git(['clone', '--branch', 'main', url, str(path)], root)
        return 'CLONED'
    if not (path / '.git').exists():
        raise ValueError('path exists without its own .git; left untouched')
    origin = git(['remote', 'get-url', 'origin'], path)
    if normalize_git_url(origin) != normalize_git_url(url):
        raise ValueError('origin differs from catalog; left untouched')
    if git(['branch', '--show-current'], path) != 'main':
        raise ValueError('not on main; left untouched')
    if git(['status', '--porcelain', '--untracked-files=normal'], path):
        raise ValueError('uncommitted files; left untouched')
    if not pull:
        return 'READY (add --pull to update)'
    # Refuse unpublished local commits as well as divergence; pull must not mask them.
    if dry_run:
        return 'WOULD FETCH AND FAST-FORWARD origin/main'
    git(['fetch', 'origin', 'main'], path)
    ahead = git(['rev-list', '--count', 'origin/main..HEAD'], path)
    if ahead != '0':
        raise ValueError('local commits are not on origin/main; left untouched')
    git(['-c', 'pull.rebase=false', 'pull', '--ff-only', 'origin', 'main'], path)
    return 'UPDATED (fast-forward only)'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--clone-missing', action='store_true')
    parser.add_argument('--pull', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--family', choices=FAMILIES)
    args = parser.parse_args()
    failures = 0
    for project in load_catalog()['projects']:
        if args.family and project['family'] != args.family:
            continue
        try:
            status = sync(project, pull=args.pull, clone_missing=args.clone_missing, dry_run=args.dry_run)
            print(project['path'] + ': ' + status)
            if status.startswith('MISSING'):
                failures += 1
        except (ValueError, OSError, subprocess.TimeoutExpired) as error:
            failures += 1
            print(project['path'] + ': BLOCKED: ' + str(error))
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())

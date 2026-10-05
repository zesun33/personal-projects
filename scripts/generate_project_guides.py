#!/usr/bin/env python3
"""Refresh the marked orientation sections in checked-out project READMEs."""
import argparse
import sys
from catalog import ROOT, GUIDE_START, GUIDE_END, load_catalog, readme_orientation, replace_block


def update_readme(text, block):
    if GUIDE_START in text or GUIDE_END in text:
        return replace_block(text, block, GUIDE_START, GUIDE_END)
    title, newline, rest = text.partition('\n')
    if not newline or not title.startswith('# '):
        raise ValueError('README must begin with a Markdown title')
    return title + '\n\n' + block + '\n' + rest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='report drift without editing')
    parser.add_argument('--project', action='append', help='limit updates to catalog project paths')
    args = parser.parse_args()
    data = load_catalog()
    names = {p['path'] for p in data['projects']}
    if args.project and not set(args.project) <= names:
        parser.error('unknown project')
    stale = []
    for p in data['projects']:
        if args.project and p['path'] not in args.project:
            continue
        path = ROOT / p['path'] / 'README.md'
        if not path.is_file():
            print(p['path'] + ': SKIP (checkout missing)')
            continue
        raw = path.read_bytes()
        newline = '\r\n' if b'\r\n' in raw else '\n'
        original = raw.decode().replace('\r\n', '\n')
        updated = update_readme(original, readme_orientation(p, data))
        if updated != original:
            stale.append(p['path'])
            if not args.check:
                path.write_bytes(updated.replace('\n', newline).encode())
    if args.check and stale:
        print('README guides need refresh: ' + ', '.join(stale))
        return 1
    print('README guides consistent' if args.check else f'Updated {len(stale)} README guides')
    return 0


if __name__ == '__main__':
    sys.exit(main())

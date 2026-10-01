#!/usr/bin/env python3
"""Generate or check workspace profiles, README catalog, STATUS, and checkout ignores."""
import argparse
import sys
from catalog import ROOT, generated_files, ignore_block, load_catalog, readme_block, replace_block


def outputs(root=ROOT):
    data = load_catalog(root)
    files = generated_files(data)
    files['README.md'] = replace_block((root / 'README.md').read_text(), readme_block(data),
        '<!-- BEGIN GENERATED PROJECT CATALOG -->', '<!-- END GENERATED PROJECT CATALOG -->')
    files['.gitignore'] = replace_block((root / '.gitignore').read_text(), ignore_block(data),
        '# BEGIN GENERATED PROJECT CHECKOUTS', '# END GENERATED PROJECT CHECKOUTS')
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='report drift without writing files')
    args = parser.parse_args()
    stale = []
    for name, content in outputs().items():
        path = ROOT / name
        if not path.exists() or path.read_text() != content:
            stale.append(name)
            if not args.check:
                path.write_text(content)
    if args.check and stale:
        print('Generated files need refresh: ' + ', '.join(stale))
        return 1
    print('Generated files consistent' if args.check else f'Updated {len(stale)} generated files')
    return 0


if __name__ == '__main__':
    sys.exit(main())

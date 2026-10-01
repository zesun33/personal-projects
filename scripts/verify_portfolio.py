#!/usr/bin/env python3
"""Run catalog-declared verification commands, with explicit coverage and optional GPU smoke."""
import argparse
import os
import shlex
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from catalog import ROOT, FAMILIES, load_catalog


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', help='show commands and coverage without running them')
    parser.add_argument('--family', choices=FAMILIES)
    parser.add_argument('--project', help='run one catalog project')
    parser.add_argument('--include-gpu', action='store_true', help='include CUDA smoke (CUDA_ARCH and CUDA_VISIBLE_DEVICES honored)')
    args = parser.parse_args()
    records = load_catalog()['projects']
    if args.project and args.project not in {p['path'] for p in records}:
        parser.error('unknown project: ' + args.project)
    selected = [p for p in records if (not args.family or p['family'] == args.family)
                and (not args.project or p['path'] == args.project)]
    if not selected:
        parser.error('no projects match the selected filters')
    failures = passed = skipped = 0
    log_root = None if args.list else Path(tempfile.mkdtemp(prefix='portfolio-verification-'))
    for p in selected:
        name = p['path']
        steps = [step[:] for step in p.get('verify_steps', [])]
        if not steps:
            print(f'{name}: NOT CONFIGURED ({p["verification"]})')
            skipped += 1
            continue
        if args.list:
            suffix = ' [requires --include-gpu]' if p.get('requires_gpu') else ''
            print(f'{name}: ' + ' -> '.join(shlex.join(step) for step in steps) + suffix)
            continue
        if p.get('requires_gpu') and not args.include_gpu:
            print(f'{name}: SKIPPED (GPU smoke is opt-in)')
            skipped += 1
            continue
        if p.get('requires_gpu') and os.environ.get('CUDA_ARCH'):
            steps[0].append('ARCH=' + os.environ['CUDA_ARCH'])
        checkout = ROOT / name
        log = log_root / (name + '.log')
        start = time.monotonic()
        result_code = 0
        with log.open('w') as output:
            for command in steps:
                output.write('$ ' + shlex.join(command) + '\n')
                output.flush()
                try:
                    result = subprocess.run(command, cwd=checkout, stdout=output, stderr=subprocess.STDOUT)
                    result_code = result.returncode
                except OSError as error:
                    output.write(str(error) + '\n')
                    result_code = 1
                if result_code:
                    break
        verdict = 'FAIL' if result_code else 'PASS'
        print(f'{name}: {verdict} ({time.monotonic() - start:.1f}s) log={log}', flush=True)
        failures += bool(result_code)
        passed += not result_code
    if not args.list:
        print(f'Coverage: {passed} passed, {failures} failed, {skipped} skipped/not configured. Logs: {log_root}')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())

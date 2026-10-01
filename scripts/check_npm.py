#!/usr/bin/env python3
"""Exercise published npx commands in a disposable directory (no EDA runs)."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from catalog import ROOT, load_catalog


def main():
    failures = 0
    with tempfile.TemporaryDirectory(prefix='portfolio-npx-') as work:
        for p in load_catalog()['projects']:
            if not p.get('npm_published'):
                continue
            version = json.loads((ROOT / p['path'] / 'package.json').read_text())['version']
            spec = p['npm_package'] + '@' + version
            try:
                if p['kind'] == 'mcp':
                    request = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/list'}) + '\n'
                    result = subprocess.run(['npx', '-y', spec], input=request, cwd=work,
                        text=True, capture_output=True, timeout=60)
                    responses = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
                    response = next((r for r in responses if r.get('id') == 1), {})
                    if result.returncode or not response.get('result', {}).get('tools'):
                        raise ValueError('tools/list failed: ' + (result.stderr or result.stdout)[-500:])
                    print(spec + ': PASS (npx + MCP tools/list)')
                elif p['kind'] == 'scaffold':
                    target = str(Path(work) / 'generated-project')
                    result = subprocess.run(['npx', '-y', spec, target], cwd=work, text=True,
                        capture_output=True, timeout=60)
                    if result.returncode:
                        raise ValueError(result.stderr)
                    servers = json.loads((Path(target) / '.cursor/mcp.json').read_text())['mcpServers']
                    expected = {x['npm_package'] for x in load_catalog()['projects'] if x['kind'] == 'mcp'}
                    if {x['args'][1] for x in servers.values()} != expected or len(servers) != len(expected):
                        raise ValueError('published scaffold MCP list differs from catalog')
                    print(spec + ': PASS (npx + generated MCP config)')
            except (ValueError, OSError, subprocess.TimeoutExpired) as error:
                failures += 1
                print(spec + ': FAIL: ' + str(error))
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())

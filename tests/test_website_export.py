"""Validate completeness and non-mutating checks across the website boundary."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from catalog import load_catalog
from export_website import document


class WebsiteExportTests(unittest.TestCase):
    def test_export_covers_catalog_and_preserves_scope(self):
        catalog = load_catalog()
        result = json.loads(document(catalog))
        self.assertEqual(len(result['projects']), len(catalog['projects']))
        for source, exported in zip(catalog['projects'], result['projects']):
            self.assertEqual(exported['guide']['scope'], source['guide']['scope'])
            self.assertTrue(exported['start_url'].startswith('https://github.com/'))
        by_name = {p['path']: p for p in result['projects']}
        self.assertEqual(by_name['cim-bit-serial-pe']['status_label'], 'Architecture draft')
        self.assertEqual(by_name['cuda-memory-benchmark']['status_label'], 'Learning exercise')

    def test_check_accepts_json_formatting_and_leaves_drift_untouched(self):
        with tempfile.TemporaryDirectory() as folder:
            site = Path(folder)
            (site / '_config.yml').write_text('title: Preview\n')
            (site / '_data').mkdir()
            command = [sys.executable, str(ROOT / 'scripts/export_website.py'), '--website', str(site)]
            subprocess.run(command, check=True, capture_output=True)
            target = site / '_data/portfolio.json'
            data = json.loads(target.read_text())
            target.write_text(json.dumps(data))
            subprocess.run(command + ['--check'], check=True, capture_output=True)
            data['projects'][0]['description'] = 'incorrect description'
            target.write_text(json.dumps(data))
            before = target.read_bytes()
            result = subprocess.run(command + ['--check'], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(target.read_bytes(), before)

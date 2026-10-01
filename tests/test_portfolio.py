"""Behavior checks for portable catalog output and safe cross-repository synchronization."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from catalog import load_catalog
from check_catalog import check
from generate_catalog import outputs
from sync_projects import sync


def git(*args, cwd):
    p = subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True)
    if p.returncode:
        raise AssertionError(p.stderr)
    return p.stdout.strip()


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.work = tempfile.TemporaryDirectory()
        self.addCleanup(self.work.cleanup)
        self.root = Path(self.work.name)
        for file in ['projects.json', 'README.md', '.gitignore']:
            shutil.copy2(ROOT / file, self.root / file)
        for file, content in outputs(self.root).items():
            (self.root / file).write_text(content)

    def test_fresh_parent_clone_without_children_passes_metadata_check(self):
        # The tracked Rust metadata directory exists even when none of the separate repositories do.
        (self.root / 'rust-systems-track').mkdir()
        errors, _ = check(self.root, catalog_only=True)
        self.assertEqual(errors, [])
        errors, _ = check(self.root)
        self.assertTrue(any('missing checkout' in e for e in errors))

    def test_generated_profile_drift_is_detected(self):
        path = self.root / 'ml-systems.code-workspace'
        ws = json.loads(path.read_text())
        ws['folders'].pop()
        path.write_text(json.dumps(ws))
        errors, _ = check(self.root, catalog_only=True)
        self.assertTrue(any('ml-systems.code-workspace' in e and 'drift' in e for e in errors))

    def test_ssh_https_origin_urls_are_equivalent(self):
        from catalog import normalize_git_url
        expected = 'https://github.com/zesun33/mcp-verilog'
        for url in [expected+'.git', 'git@github.com:zesun33/mcp-verilog.git',
                    'ssh://git@github.com/zesun33/mcp-verilog.git']:
            self.assertEqual(normalize_git_url(url), expected)

    def test_invalid_path_is_rejected_before_sync(self):
        data = json.loads((self.root / 'projects.json').read_text())
        data['projects'][0]['path'] = '../outside'
        (self.root / 'projects.json').write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'Invalid'):
            load_catalog(self.root)


    def test_verification_runner_reports_failure_and_uncovered_projects(self):
        scripts = self.root / 'scripts'
        scripts.mkdir()
        for name in ['catalog.py', 'verify_portfolio.py']:
            shutil.copy2(ROOT / 'scripts' / name, scripts / name)
        data = json.loads((self.root / 'projects.json').read_text())
        selected = [p for p in data['projects'] if p['path'] in {'hw-agent-scaffold', 'resnet-tensorrt-bench'}]
        for p in selected:
            if p['path'] == 'hw-agent-scaffold':
                p['verify_steps'] = [[sys.executable, '-c', 'raise SystemExit(3)']]
            (self.root / p['path']).mkdir()
        data['projects'] = selected
        data['profiles'] = {}
        (self.root / 'projects.json').write_text(json.dumps(data))
        result = subprocess.run([sys.executable, str(scripts / 'verify_portfolio.py')],
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('hw-agent-scaffold: FAIL', result.stdout)
        self.assertIn('resnet-tensorrt-bench: NOT CONFIGURED', result.stdout)
        self.assertIn('0 passed, 1 failed, 1 skipped/not configured', result.stdout)


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.work = tempfile.TemporaryDirectory()
        self.addCleanup(self.work.cleanup)
        self.root = Path(self.work.name)
        self.remote = self.root / 'remote.git'
        self.source = self.root / 'source'
        self.destination = self.root / 'destination'
        self.destination.mkdir()
        self.source.mkdir()
        git('init', '--bare', '--initial-branch=main', str(self.remote), cwd=self.root)
        git('init', '--initial-branch=main', cwd=self.source)
        git('config', 'user.name', 'Test Author', cwd=self.source)
        git('config', 'user.email', 'test@example.invalid', cwd=self.source)
        (self.source / 'README.md').write_text('first\n')
        git('add', 'README.md', cwd=self.source)
        git('commit', '-m', 'initial', cwd=self.source)
        git('remote', 'add', 'origin', str(self.remote), cwd=self.source)
        git('push', 'origin', 'main', cwd=self.source)
        self.project = {'path': 'project', 'github': str(self.remote)}

    def clone(self):
        return sync(self.project, self.destination, clone_missing=True)

    def advance(self):
        (self.source / 'README.md').write_text('second\n')
        git('commit', '-am', 'advance', cwd=self.source)
        git('push', 'origin', 'main', cwd=self.source)

    def test_clone_and_fast_forward(self):
        self.assertEqual(self.clone(), 'CLONED')
        self.advance()
        self.assertIn('UPDATED', sync(self.project, self.destination, pull=True))
        self.assertEqual((self.destination / 'project/README.md').read_text(), 'second\n')

    def test_dry_run_does_not_clone(self):
        self.assertIn('WOULD CLONE', sync(self.project, self.destination, clone_missing=True, dry_run=True))
        self.assertFalse((self.destination / 'project').exists())

    def test_dirty_and_non_git_paths_are_untouched(self):
        self.clone()
        checkout = self.destination / 'project'
        (checkout / 'local.txt').write_text('keep this\n')
        with self.assertRaisesRegex(ValueError, 'uncommitted'):
            sync(self.project, self.destination, pull=True)
        self.assertEqual((checkout / 'local.txt').read_text(), 'keep this\n')
        ordinary = self.destination / 'ordinary'
        ordinary.mkdir()
        with self.assertRaisesRegex(ValueError, 'without its own'):
            sync({'path': 'ordinary', 'github': str(self.remote)}, self.destination, pull=True)

    def test_unpublished_commits_and_wrong_branch_are_untouched(self):
        self.clone()
        checkout = self.destination / 'project'
        git('config', 'user.name', 'Test Author', cwd=checkout)
        git('config', 'user.email', 'test@example.invalid', cwd=checkout)
        (checkout / 'README.md').write_text('local-only\n')
        git('commit', '-am', 'local-only', cwd=checkout)
        head = git('rev-parse', 'HEAD', cwd=checkout)
        with self.assertRaisesRegex(ValueError, 'local commits'):
            sync(self.project, self.destination, pull=True)
        self.assertEqual(git('rev-parse', 'HEAD', cwd=checkout), head)
        git('switch', '-c', 'work', cwd=checkout)
        with self.assertRaisesRegex(ValueError, 'not on main'):
            sync(self.project, self.destination, pull=True)

    def test_wrong_remote_is_untouched(self):
        self.clone()
        checkout = self.destination / 'project'
        git('remote', 'set-url', 'origin', 'https://example.invalid/wrong.git', cwd=checkout)
        with self.assertRaisesRegex(ValueError, 'origin differs'):
            sync(self.project, self.destination, pull=True)


if __name__ == '__main__':
    unittest.main()

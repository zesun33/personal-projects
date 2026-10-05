"""Protect existing npm publishers and reject incomplete/conflicting responses."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from setup_npm_trust import inspect, matches, parse_configs


class NpmTrustTests(unittest.TestCase):
    project = {'npm_package': '@zesun33/mcp-rtl-review',
               'github': 'https://github.com/zesun33/mcp-rtl-review'}
    config = {'type': 'github', 'repository': 'zesun33/mcp-rtl-review',
              'file': 'publish.yml', 'permissions': ['createPackage']}

    def test_existing_match_is_not_scheduled_for_creation(self):
        with patch('setup_npm_trust.list_configs', return_value=[self.config]):
            self.assertEqual(inspect([self.project]), [])

    def test_conflicting_workflow_stops_batch(self):
        config = {**self.config, 'file': 'other.yml'}
        with patch('setup_npm_trust.list_configs', return_value=[config]):
            with self.assertRaisesRegex(ValueError, 'existing trust differs'):
                inspect([self.project])

    def test_restrictions_and_permissions_must_match(self):
        for changes in [{'environment': 'production'}, {'repository': 'other/repo'},
                        {'permissions': ['createStagedPackage']}, {'permissions': []},
                        {'permissions': ['createPackage', 'manageDistTags']}]:
            self.assertFalse(matches({**self.config, **changes}, self.project))

    def test_server_added_staging_permission_is_accepted(self):
        self.assertTrue(matches({**self.config,
                               'permissions': ['createPackage', 'createStagedPackage']},
                               self.project))

    def test_cli_empty_and_multiple_json_responses(self):
        self.assertEqual(parse_configs(''), [])
        self.assertEqual(len(parse_configs('{"id":"a"}\n{"id":"b"}')), 2)
        with self.assertRaises(ValueError):
            parse_configs('not a trust configuration')

    def test_authorization_failure_is_not_treated_as_missing(self):
        with patch('setup_npm_trust.list_configs', side_effect=RuntimeError('401')):
            with self.assertRaisesRegex(RuntimeError, '401'):
                inspect([self.project])


if __name__ == '__main__':
    unittest.main()

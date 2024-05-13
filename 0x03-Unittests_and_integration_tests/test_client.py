#!/usr/bin/env python3
"""This module contains the test cases for the Github"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method of GithubOrgClient class."""
        mock_get_json.return_value = {"name": org_name}
        github_client = GithubOrgClient(org_name)
        result = github_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, {"name": org_name})

if __name__ == '__main__':
    unittest.main()

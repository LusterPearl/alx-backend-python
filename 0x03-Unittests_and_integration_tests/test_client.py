#!/usr/bin/env python3
"""Test cases for the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method of GithubOrgClient class."""
        mock_get_json.return_value = {"name": org_name}

        """Create an instance of GithubOrgClient"""
        github_client = GithubOrgClient(org_name)

        """Call the org method"""
        result = github_client.org()

        """Assert that get_json was called once with the correct argument"""
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        self.assertEqual(result, {"name": org_name})

if __name__ == "__main__":
    unittest.main()

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

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property of GithubOrgClient class."""
        mock_org.return_value = {"public_repos": 10}

        github_client = GithubOrgClient("org_name")

        result = github_client._public_repos_url

        expected_url = "https://api.github.com/orgs/org_name/repos"
        self.assertEqual(result, expected_url)        


if __name__ == "__main__":
    unittest.main()

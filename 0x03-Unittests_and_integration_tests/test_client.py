#!/usr/bin/env python3
"""This module contains the test cases for the Github"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([('google',), ('abc',)])
    @patch('client.GithubOrgClient._public_repos_url')
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json, mock_url):
        """Test the org property of GithubOrgClient."""
        mock_url.return_value = f'https://api.github.com/orgs/{org_name}/repos'
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, f'https://api.github.com/orgs/{org_name}')
        mock_url.assert_called_once_with()
        mock_get_json.assert_not_called()


if __name__ == '__main__':
    unittest.main()

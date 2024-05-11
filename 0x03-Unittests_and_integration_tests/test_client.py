#!/usr/bin/env python3
"""Test cases for the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method of GithubOrgClient class."""
        github_client = GithubOrgClient("org_name")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(("org_payload", "repos_payload", "expected_repos",
                      "apache2_repos"),
                     [(org_payload, repos_payload, expected_repos,
                        apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class with mock responses."""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        cls.get_patcher.stop()

    def setUp(self):
        """Set up the test."""
        self.github_client = GithubOrgClient("test_org")

    def test_public_repos(self):
        """Test public_repos method of GithubOrgClient class."""
        self.mock_get.side_effect = [org_payload, repos_payload]
        result = self.github_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_apache2_repos(self):
        """Test apache2_repos method of GithubOrgClient class."""
        self.mock_get.side_effect = [org_payload, repos_payload]
        result = self.github_client.apache2_repos()
        self.assertEqual(result, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()

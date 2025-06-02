#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
import requests
from client import GithubOrgClient
import fixtures


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (
            fixtures.org_payload,
            fixtures.repos_payload,
            fixtures.expected_repos,
            fixtures.apache2_repos,
        )
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Setup patcher for requests.get to mock API responses"""

        def get_side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            if url == cls.org_payload["repos_url"]:
                mock_resp.json.return_value = cls.repos_payload
            elif url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                mock_resp.json.return_value = cls.org_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        cls.get_patcher = patch("requests.get", side_effect=get_side_effect)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repos list"""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering repos by license key"""
        client = GithubOrgClient(self.org_payload["login"])
        apache2_repos = client.public_repos(license_key="apache-2.0")
        self.assertEqual(apache2_repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()

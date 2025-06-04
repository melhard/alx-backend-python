#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        # Arrange: setup mock return value (can be anything, e.g., empty dict)
        mock_get_json.return_value = {}

        # Act
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert get_json was called once with the right URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Assert the org property returns the mocked value
        self.assertEqual(result, {})


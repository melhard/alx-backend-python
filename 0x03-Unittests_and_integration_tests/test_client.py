#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """اختبار GithubOrgClient"""
    def test_public_repos_url(self):
    """اختبار أن _public_repos_url تُرجع الرابط الصحيح من org"""

    payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

    with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
        mock_org.return_value = payload

        client = GithubOrgClient("testorg")
        result = client._public_repos_url

        self.assertEqual(result, payload["repos_url"])


    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """تأكد أن org تستدعي get_json بالمسار الصحيح"""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        # تأكد أن get_json تم استدعاؤها مرة واحدة بالمسار الصحيح
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        # تأكد من أن النتيجة المرجعة صحيحة
        self.assertEqual(result, test_payload)

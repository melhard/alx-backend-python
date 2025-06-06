#!/usr/bin/env python3

"""
وحدة اختبار تشمل دوال utils:
- access_nested_map: اختبار للوصول إلى القيم المتداخلة في القواميس.
- get_json: اختبار لجلب البيانات من URL باستخدام JSON.
- memoize: اختبار لتخزين نتائج الدوال.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """اختبار دالة access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """تأكد أن access_nested_map ترجع القيمة المتوقعة من القاموس."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """اختبار دالة get_json."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """تأكد أن get_json ترجع البيانات المتوقعة مع محاكاة requests.get."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("requests.get", return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """اختبار دالة memoize."""

    def test_memoize(self):
        """تأكد أن memoize تحفظ وتعيد القيمة بشكل صحيح."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()

        self.assertEqual(obj.a_property, 42)

#!/usr/bin/env python3#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """اختبارات لدالة access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")


class TestGetJson(unittest.TestCase):
    """اختبارات لدالة get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("utils.requests.get", return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
            from utils import memoize


class TestMemoize(unittest.TestCase):
    """اختبار المزخرف memoize"""

    def test_memoize(self):
        """تأكد أن memoize يخزن القيمة ولا يستدعي الدالة إلا مرة واحدة"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()

            # أول استدعاء
            result1 = obj.a_property()
            # ثاني استدعاء (يجب ألا يستدعي a_method مرة أخرى)
            result2 = obj.a_property()

            # تأكد من النتيجة صحيحة
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # تأكد أن a_method تم استدعاؤها مرة واحدة فقط
            mock_method.assert_called_once()


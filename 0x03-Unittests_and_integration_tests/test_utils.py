#!/usr/bin/env python3
"""
Test for memoize decorator
"""

import unittest
from unittest.mock import MagicMock

def memoize(fn):
    """Memoize decorator"""
    cache = {}

    def memoized_fn(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return memoized_fn


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""

    def test_memoize(self):
        """Test memoize caches results"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()
        obj.a_method = MagicMock(return_value=42)

        # Call the memoized method twice
        result1 = obj.a_property()
        result2 = obj.a_property()

        # Assert the value returned is correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        # Assert a_method was called only once because of memoization
        obj.a_method.assert_called_once()

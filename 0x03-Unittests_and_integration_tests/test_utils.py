#!/usr/bin/env python3

"""
Module that contains unit tests for the 'access_nested_map' function
in the 'utils' module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    A test case class for the 'access_nested_map' function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test method to verify the behavior of the 'access_nested_map' function

        Args:
            nested_map (dict):nested dictionery to be accessed
            path (tuple): path to the nested key
            expected_result: expected result after accessing the nested key

        Returns:
            None
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

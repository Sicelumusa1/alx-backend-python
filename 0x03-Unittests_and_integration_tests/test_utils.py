#!/usr/bin/env python3

"""
Module that contains unit tests for the 'access_nested_map' function
in the 'utils' module
"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    A test case class for the 'access_nested_map' function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        """
        Test method to verify the behavior of the 'access_nested_map' function
        when encountering exceptions

        Args:
            nested_map (dict):nested dictionery to be accessed
            path (tuple): path to the nested key
            expected_exception: expected exception when accessing
            the nested key
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertIsInstance(context.exception, expected_exception)


class TestGetJson(unittest.TestCase):
    """
    A test case class for the 'get_json' function
    """
    @patch('requests.get')
    def test_get_json(self, mock_request_get):
        """
        Test the 'get_json' function

        Args:
            mock_request_get (MagicMock): A mock object for 'request.get'
        """
        test_url1 = "http://example.com"
        test_payload1 = {"payload": True}
        test_url2 = "http://holberton.io"
        test_payload2 = {"payload": False}

        # Configure the mock response for each URL
        mock_response1 = MagicMock()
        mock_response1.json.return_value = test_payload1

        mock_response2 = MagicMock()
        mock_response2.json.return_value = test_payload2

        mock_request_get.side_effect = [mock_response1, mock_response2]

        # Call function under test
        result1 = get_json(test_url1)
        result2 = get_json(test_url2)

        # Assert that requests.get was called exactly once with
        # the correct URL
        mock_request_get.assert_has_calls([
            unittest.mock.call(test_url1),
            unittest.mock.call(test_url2)
        ])

        # Assert that the output matches the expected payload
        self.assertEqual(result1, test_payload1)
        self.assertEqual(result2, test_payload2)


class TestMemoize(unittest.TestCase):
    """
    A test case class for the ''memoize' decorator
    """
    class TestClass:
        """
        A class to test memoization
        """
        def a_method(self):
            """
            A method to be memoized
            """
            return 42

        @memoize
        def a_property(self):
            """
            A memoize property
            """
            return self.a_method()

        def test_memoize(self):
            """
            Test method to verify memoization behavior
            """
            # Create an instance of TestClass
            test_instance = self.TestClass()

            # Mock the a_method
            with patch.object(test_instance, 'a_method') as mock_a_method:
                # Set the return value for the mock
                mock_a_method. return_value = 42

                # Access the a_property twice
                result1 = test_instance.a_property
                result2 = test_instance.a_property

                # Assert that a_method was called only once
                mock_a_method.assert_called_once()

                # Assert that the results are equal
                self.assertEqual(result1, 42)
                self.assertEqual(result2, 42)

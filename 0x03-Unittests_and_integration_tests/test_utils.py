#!/usr/bin/env python3
""" Testing whether the method returns the expected output """

import unittest
from unittest.mock import patch, Mock
from typing import Any, Mapping, Sequence
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Testing whether the method returns the expected output """

    @parameterized.expand([
        ({'a': 1}, ('a'), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence,
            expected_output: Any) -> None:
        """ Testing whether the method returns the expected output """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence,
            expected_output: str) -> None:
        """ Testing whether the method returns the expected error """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), f"'{expected_output}'")


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """Test that get_json returns the expected result."""
        # Patch requests.get so no real HTTP call is made
        with patch("utils.requests.get") as mock_get:
            # Configure the mock to return a mock response
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json with the test_url
            result = get_json(test_url)

            # Verify that requests.get was called once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Check that the returned value matches the expected payload
            self.assertEqual(result, test_payload)


class TestMemoize(Unittest.TestCase):
    """ A memoization class """

    def test_memoize(self):
        """ Test memoize decorator on a_property"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """ Method that returns a_method """
                return self.a_method()

        # Instantiate TestClass
        test_instance = TestClass()

        # Patch a_method so we can monitor its calls
        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_method:
            # Access a_property twice
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            # Check the result is as expected
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)

            # Ensure a_method was called only once
            mock_method.assert_called_once()

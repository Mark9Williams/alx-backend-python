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

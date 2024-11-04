#!/usr/bin/env python3
""" Testing whether the method returns the expected output """

import unittest
from typing import Any, Mapping, Sequence
from parameterized import parameterized
from utils import access_nested_map


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
    def test_access_nested_map_raise(
            self, nested_map: Mapping, path: Sequence,
            expected_output: str) -> None:
        """ Testing whether the method returns the expected error """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), f"'{expected_output}'")

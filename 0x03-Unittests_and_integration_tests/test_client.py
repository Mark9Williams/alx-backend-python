#!/usr/bin/env python3
""" Validating the GithubOrgClient.org method returns the expected result """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import List, Dict


class TestGithurbOrgClient(unittest.TestCase):
    """ Testing whether the method returns the expected output """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', autospec=True)
    def test_org(self, org_name: str, expected_output: Dict,
                 mock_get_json: Mock) -> None:
        """ Testing whether the method returns the expected output """
        mock_get_json.return_value = expected_output
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_output)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

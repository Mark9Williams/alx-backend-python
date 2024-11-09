#!/usr/bin/env python3
""" Validating the GithubOrgClient.org method returns the expected result """

import unittest
from typing import Dict
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1,
         "repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"login": "abc", "id": 2,
         "repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json', autospec=True)
    def test_org(self, org_name: str,
                 expected_result: Dict, mock_get_json) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        # Set the mock return value
        mock_get_json.return_value = expected_result

        # Instantiate GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)
        result = client.org

        # Assertions to check that org property works as expected
        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self) -> None:
        """Test that the _public_repos_url method returns the expected"""
        # set up the expected result
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        with patch('client.GithubOrgClient.org',
                   return_value=mock_payload):
            # Instantiate GithubOrgClient with the org_name
            client = GithubOrgClient("google")
            expected_result = "https://api.github.com/orgs/google/repos"

            # checking that _public_repos_url property works as expected
            self.assertEqual(client._public_repos_url, expected_result)


if __name__ == "__main__":
    unittest.main()

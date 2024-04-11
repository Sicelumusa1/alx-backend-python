#!/usr/bin/env python3

"""
Module containig unit tests for the 'GithubOrgClient' class
in the 'client' module
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case class for the 'GithubOrgClient' class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test method to verify the behavior of the 'org' method in the
        'GithubOrgClient' class

        Args:
            org_name (str): the name of the organization to be tested
            mock_get_json (MagicMock): The mocked 'get_json' function
        """
        expected_url = f'https://api.github.com/orgs/{org_name}'

        # Mock the return value of get_json
        mock_get_json.return_value = {'org_data': 'mocked_data'}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the method under test
        result = client.org()

        # Assert that get_json was called once
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {"org_data": "mocked_data"})

    def test_public_repos_url(self):
        """
        """
        org_name = "example_org"
        client = GithubOrgClient(org_name)

        # Mock the org method to return a known payload
        expected_payload = {"repos_url": "https://api.github.com/"
                            "example_org/repos"}
        with patch.object(client, 'org', return_value=expected_payload):
            # Call the method under test
            result = client._public_repos_url()

            # Assert that the result matches the expected repos URL
            self.assertEqual(result, expected_payload["repos_url"])

    @parameterized.expand([
        ({"license": {"key": "my_licence"}}, "my_license", True),
        ({"license": {"key": "other_licence"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test if the GithubOrgClient.has_license() method correctly determines
        whether a repository has a specific license key

        Args:
            repo (dict): A dictionary representing the repo to be tested
            license_key (str): The license to be checked for in a repo
            expected_result (bool): The expected outcome of the method
        """
        # Create an instance of GithubOrgClient
        org_name = "example_org"
        client = GithubOrgClient(org_name)

        # Call the method under test
        result = client.has_license(repo, license_key)

        # Assert that the result matches the expected value
        self.assertEqual(result, expected_result)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient class
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the class by patching the 'request.get' method
        to return example payloads.
        """
        # Mock request.get to return example payloads
        cls.get_patcher = patch('requests.get')
        cls.mock_requests_get = cls.get_patcher.start()
        cls.mock_requests_get.side_effect = [
            org_payload,
            rrepos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after the test class by stopping the patching of
        'request.get'
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the 'public_repos' method of GithubOrgClient without
        specifying a license
        """
        org_name = "example_org"
        client = GithubOrgClient(org_name)

        # Call the method under test
        result = client.public_repos()

        # Assert that the result matches the expected repos
        self.assertEqual(result, expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the 'public_repos' method of GithubOrgClient with a
        specific license
        """
        org_name = "example_org"
        client = GithubOrgClient(org_name)

        # Call the method with a specific license
        result = client.public_repos(license="apache-2.0")

        # Assert that the result matches the expected apache2_repos
        seld.assertEqual(result, apache2_repos)

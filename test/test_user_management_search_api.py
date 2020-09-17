# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.user_management_search_api import UserManagementSearchApi


class TestUserManagementSearchApi(unittest.TestCase):
    """ UserManagementSearchApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.user_management_search_api.UserManagementSearchApi()

    def tearDown(self):
        pass

    def test_search_users(self):
        """
        Test case for search_users

        Search User Information
        """
        pass


if __name__ == '__main__':
    unittest.main()
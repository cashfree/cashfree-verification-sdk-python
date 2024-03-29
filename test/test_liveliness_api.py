# coding: utf-8

"""
    Cashfree Verification API's.

    Cashfree's Verification APIs provide different types of verification to our merchants.

    The version of the OpenAPI document: 2023-12-18
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import cashfree_verification
from cashfree_verification.api.liveliness_api import LivelinessApi  # noqa: E501
from cashfree_verification.rest import ApiException


class TestLivelinessApi(unittest.TestCase):
    """LivelinessApi unit test stubs"""

    def setUp(self):
        self.api = cashfree_verification.api.liveliness_api.LivelinessApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_vrs_liveliness_check(self):
        """Test case for vrs_liveliness_check

        Liveliness Check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

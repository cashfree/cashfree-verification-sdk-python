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
from cashfree_verification.api.pan_api import PANApi  # noqa: E501
from cashfree_verification.rest import ApiException


class TestPANApi(unittest.TestCase):
    """PANApi unit test stubs"""

    def setUp(self):
        self.api = cashfree_verification.api.pan_api.PANApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_vrs_bulk_pan_verification(self):
        """Test case for vrs_bulk_pan_verification

        Verify PAN in Bulk  # noqa: E501
        """
        pass

    def test_vrs_fetch_bulk_pan_details(self):
        """Test case for vrs_fetch_bulk_pan_details

        Get Status for Verify PAN in Bulk  # noqa: E501
        """
        pass

    def test_vrs_fetch_pan_details(self):
        """Test case for vrs_fetch_pan_details

        Get Status of Verify PAN Sync  # noqa: E501
        """
        pass

    def test_vrs_pan_advance_verification(self):
        """Test case for vrs_pan_advance_verification

        PAN 360  # noqa: E501
        """
        pass

    def test_vrs_pan_ocr_verification(self):
        """Test case for vrs_pan_ocr_verification

        PAN Verification via OCR  # noqa: E501
        """
        pass

    def test_vrs_pan_verification(self):
        """Test case for vrs_pan_verification

        Verify PAN Sync  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

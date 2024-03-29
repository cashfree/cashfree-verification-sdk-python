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
import datetime

import cashfree_verification
from cashfree_verification.models.driving_license_response_schema_dl_validity import DrivingLicenseResponseSchemaDlValidity  # noqa: E501
from cashfree_verification.rest import ApiException

class TestDrivingLicenseResponseSchemaDlValidity(unittest.TestCase):
    """DrivingLicenseResponseSchemaDlValidity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DrivingLicenseResponseSchemaDlValidity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DrivingLicenseResponseSchemaDlValidity`
        """
        model = cashfree_verification.models.driving_license_response_schema_dl_validity.DrivingLicenseResponseSchemaDlValidity()  # noqa: E501
        if include_optional :
            return DrivingLicenseResponseSchemaDlValidity(
                non_transport = {"value":{"to":"2023-10-23","from":"2023-10-23"}}, 
                hazardous_valid_till = 'Tue Oct 23 00:00:00 UTC 2001', 
                transport = {"value":{"to":"2023-10-23","from":"2023-10-23"}}, 
                hill_valid_till = 'Tue Oct 23 00:00:00 UTC 2001'
            )
        else :
            return DrivingLicenseResponseSchemaDlValidity(
        )
        """

    def testDrivingLicenseResponseSchemaDlValidity(self):
        """Test DrivingLicenseResponseSchemaDlValidity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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
from cashfree_verification.models.upi_advance_request_schema import UpiAdvanceRequestSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestUpiAdvanceRequestSchema(unittest.TestCase):
    """UpiAdvanceRequestSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpiAdvanceRequestSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpiAdvanceRequestSchema`
        """
        model = cashfree_verification.models.upi_advance_request_schema.UpiAdvanceRequestSchema()  # noqa: E501
        if include_optional :
            return UpiAdvanceRequestSchema(
                vpa = 'valid_vpa@upi', 
                name = 'John Doe'
            )
        else :
            return UpiAdvanceRequestSchema(
                vpa = 'valid_vpa@upi',
        )
        """

    def testUpiAdvanceRequestSchema(self):
        """Test UpiAdvanceRequestSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

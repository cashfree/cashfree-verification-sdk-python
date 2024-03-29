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
from cashfree_verification.models.upi_mobile_request_schema import UpiMobileRequestSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestUpiMobileRequestSchema(unittest.TestCase):
    """UpiMobileRequestSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpiMobileRequestSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpiMobileRequestSchema`
        """
        model = cashfree_verification.models.upi_mobile_request_schema.UpiMobileRequestSchema()  # noqa: E501
        if include_optional :
            return UpiMobileRequestSchema(
                verification_id = 'test_verification_id', 
                mobile_number = '6666666666', 
                name = 'John Doe', 
                email = 'JohnDoe@gmail.com'
            )
        else :
            return UpiMobileRequestSchema(
                verification_id = 'test_verification_id',
                mobile_number = '6666666666',
        )
        """

    def testUpiMobileRequestSchema(self):
        """Test UpiMobileRequestSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

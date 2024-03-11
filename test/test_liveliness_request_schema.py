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
from cashfree_verification.models.liveliness_request_schema import LivelinessRequestSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestLivelinessRequestSchema(unittest.TestCase):
    """LivelinessRequestSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LivelinessRequestSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LivelinessRequestSchema`
        """
        model = cashfree_verification.models.liveliness_request_schema.LivelinessRequestSchema()  # noqa: E501
        if include_optional :
            return LivelinessRequestSchema(
                verification_id = '123', 
                image = '[B@74bcf1ab', 
                strict_check = True
            )
        else :
            return LivelinessRequestSchema(
                verification_id = '123',
                image = '[B@74bcf1ab',
        )
        """

    def testLivelinessRequestSchema(self):
        """Test LivelinessRequestSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

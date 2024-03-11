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
from cashfree_verification.models.digi_locker_verification_create_url_response_schema import DigiLockerVerificationCreateUrlResponseSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestDigiLockerVerificationCreateUrlResponseSchema(unittest.TestCase):
    """DigiLockerVerificationCreateUrlResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DigiLockerVerificationCreateUrlResponseSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DigiLockerVerificationCreateUrlResponseSchema`
        """
        model = cashfree_verification.models.digi_locker_verification_create_url_response_schema.DigiLockerVerificationCreateUrlResponseSchema()  # noqa: E501
        if include_optional :
            return DigiLockerVerificationCreateUrlResponseSchema(
                verification_id = 'ABC00123', 
                reference_id = 12345, 
                url = 'DIGILOCKER_URL', 
                status = 'PENDING', 
                document_requested = ["AADHAAR"], 
                redirect_url = 'REDIRECT_URL'
            )
        else :
            return DigiLockerVerificationCreateUrlResponseSchema(
        )
        """

    def testDigiLockerVerificationCreateUrlResponseSchema(self):
        """Test DigiLockerVerificationCreateUrlResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
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
from cashfree_verification.models.face_match_request_schema import FaceMatchRequestSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestFaceMatchRequestSchema(unittest.TestCase):
    """FaceMatchRequestSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FaceMatchRequestSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FaceMatchRequestSchema`
        """
        model = cashfree_verification.models.face_match_request_schema.FaceMatchRequestSchema()  # noqa: E501
        if include_optional :
            return FaceMatchRequestSchema(
                verification_id = '12345678', 
                first_image = '[B@1c0fe6c5', 
                second_image = '[B@61607ff0', 
                threshold = '0.5', 
                detect_mask_first_image = True, 
                detect_mask_second_image = True, 
                align_horizontally = True
            )
        else :
            return FaceMatchRequestSchema(
                verification_id = '12345678',
                first_image = '[B@1c0fe6c5',
                second_image = '[B@61607ff0',
        )
        """

    def testFaceMatchRequestSchema(self):
        """Test FaceMatchRequestSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

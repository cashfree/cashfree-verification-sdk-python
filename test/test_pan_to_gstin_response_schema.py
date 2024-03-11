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
from cashfree_verification.models.pan_to_gstin_response_schema import PanToGstinResponseSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestPanToGstinResponseSchema(unittest.TestCase):
    """PanToGstinResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PanToGstinResponseSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PanToGstinResponseSchema`
        """
        model = cashfree_verification.models.pan_to_gstin_response_schema.PanToGstinResponseSchema()  # noqa: E501
        if include_optional :
            return PanToGstinResponseSchema(
                reference_id = 1358, 
                verification_id = 'testverificationid', 
                status = 'SUCCESS', 
                message = 'Gstins List found', 
                pan = 'AZJPG7110R', 
                gstin_list = [
                    cashfree_verification.models.pan_to_gstin_response_schema_gstin_list_inner.PanToGstinResponseSchema_gstin_list_inner(
                        gstin = '29AAFCD5862R1ZR', 
                        status = 'ACTIVE', 
                        state = 'KARNATAKA', )
                    ]
            )
        else :
            return PanToGstinResponseSchema(
        )
        """

    def testPanToGstinResponseSchema(self):
        """Test PanToGstinResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

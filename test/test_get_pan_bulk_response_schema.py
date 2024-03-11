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
from cashfree_verification.models.get_pan_bulk_response_schema import GetPanBulkResponseSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestGetPanBulkResponseSchema(unittest.TestCase):
    """GetPanBulkResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetPanBulkResponseSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPanBulkResponseSchema`
        """
        model = cashfree_verification.models.get_pan_bulk_response_schema.GetPanBulkResponseSchema()  # noqa: E501
        if include_optional :
            return GetPanBulkResponseSchema(
                bulk_verification_id = '1123456', 
                reference_id = '515', 
                count = 1, 
                entries = {"father_name":"John Doe","message":"VALID","name_match_result":"PARTIAL","name_match_score":"0.7","name_provided":"John De","pan":"ABCDP3011E","reference_id":1234567,"registered_name":"John Doe","status_code":"VALID","type":"Individual","valid":true}
            )
        else :
            return GetPanBulkResponseSchema(
        )
        """

    def testGetPanBulkResponseSchema(self):
        """Test GetPanBulkResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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
from cashfree_verification.models.ip_verification_response_schema import IpVerificationResponseSchema  # noqa: E501
from cashfree_verification.rest import ApiException

class TestIpVerificationResponseSchema(unittest.TestCase):
    """IpVerificationResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IpVerificationResponseSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpVerificationResponseSchema`
        """
        model = cashfree_verification.models.ip_verification_response_schema.IpVerificationResponseSchema()  # noqa: E501
        if include_optional :
            return IpVerificationResponseSchema(
                reference_id = 1358, 
                verification_id = 'testverificationid', 
                status = 'VALID', 
                ip_address = '1.0.171.255', 
                proxy_type = 'VPA', 
                country_code = 'TH', 
                country_name = 'Thailand', 
                region_name = 'Phangnga', 
                city_name = 'Phang Nga', 
                city_risk_score = '0', 
                proxy_type_risk_score = '0'
            )
        else :
            return IpVerificationResponseSchema(
        )
        """

    def testIpVerificationResponseSchema(self):
        """Test IpVerificationResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

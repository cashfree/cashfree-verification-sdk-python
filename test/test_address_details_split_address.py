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
from cashfree_verification.models.address_details_split_address import AddressDetailsSplitAddress  # noqa: E501
from cashfree_verification.rest import ApiException

class TestAddressDetailsSplitAddress(unittest.TestCase):
    """AddressDetailsSplitAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressDetailsSplitAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressDetailsSplitAddress`
        """
        model = cashfree_verification.models.address_details_split_address.AddressDetailsSplitAddress()  # noqa: E501
        if include_optional :
            return AddressDetailsSplitAddress(
                district = [
                    '["Bangalore"]'
                    ], 
                state = [
                    [
                        '["Karnataka","KA"]'
                        ]
                    ], 
                city = [
                    'Banaglore'
                    ], 
                pincode = '560109', 
                country = [
                    '["INDIA","IND"]'
                    ], 
                address_line = 'S-90 SunTower, GopiNagar, Banaglore, KA - 560109'
            )
        else :
            return AddressDetailsSplitAddress(
        )
        """

    def testAddressDetailsSplitAddress(self):
        """Test AddressDetailsSplitAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
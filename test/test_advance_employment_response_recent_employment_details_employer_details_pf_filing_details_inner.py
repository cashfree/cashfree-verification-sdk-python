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
from cashfree_verification.models.advance_employment_response_recent_employment_details_employer_details_pf_filing_details_inner import AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner  # noqa: E501
from cashfree_verification.rest import ApiException

class TestAdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner(unittest.TestCase):
    """AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner`
        """
        model = cashfree_verification.models.advance_employment_response_recent_employment_details_employer_details_pf_filing_details_inner.AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner()  # noqa: E501
        if include_optional :
            return AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner(
                total_amount = 37524, 
                employees_count = 17, 
                wage_month = 'NOV-23'
            )
        else :
            return AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner(
        )
        """

    def testAdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner(self):
        """Test AdvanceEmploymentResponseRecentEmploymentDetailsEmployerDetailsPfFilingDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

import uuid
from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.init_partners import CreditCardDataCore, InitPartnerRequest
from papi_sdk.tests.mocked_data.init_partners import (
    init_partner_error_response,
    init_partner_ok_response,
)
from papi_sdk.tests.test_base import BaseTest


class TestHotelInfo(BaseTest):
    request_data = InitPartnerRequest(
        **{
            "object_id": "1243546",
            "pay_uuid": str(uuid.uuid4()),
            "init_uuid": str(uuid.uuid4()),
            "cvc": "123",
            "is_cvc_required": True,
            "user_first_name": "Ostrovok",
            "user_last_name": "Ostrovok",
            "credit_card_data_core": CreditCardDataCore(
                **{
                    "year": "22",
                    "card_number": "1111111111111111",
                    "card_holder": "TEST",
                    "month": "01",
                }
            ),
        }
    )

    @patch("papi_sdk.APIv3._post_request")
    def test_ok(self, m_post):
        m_post.return_value = init_partner_ok_response
        result = self.client.init_partners(data=self.request_data)

        self.assertEqual(result.status.value, self.status_ok)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.init_partners(data=InitPartnerRequest())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.init_partners()

    @patch("papi_sdk.APIv3._post_request")
    def test_error_invalid_cvc(self, m_post):
        m_post.return_value = init_partner_error_response
        result = self.client.init_partners(data=self.request_data)

        self.assertEqual(result.status.value, self.status_error)

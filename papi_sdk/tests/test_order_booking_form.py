from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.order_booking_form import (
    AffiliateHotelOrderBookingFormData,
    B2BHotelOrderBookingFormData,
    OrderBookingFormRequest,
)
from papi_sdk.tests.mocked_data.order_booking_form import (
    affiliate_order_booking_form_response,
    b2b_order_booking_form_response,
    order_booking_form_error,
)
from papi_sdk.tests.test_base import BaseTest


class TestOrderBookingForm(BaseTest):
    request = OrderBookingFormRequest(
        **{
            "partner_order_id": "test_01",
            "book_hash": "h-6d8af67c-33c8-5271-896d-f318048f86f4",
            "language": "en",
            "user_ip": "8.8.8.8",
        }
    )

    @patch("papi_sdk.APIv3._post_request")
    def test_b2b_ok(self, m_post):
        m_post.return_value = b2b_order_booking_form_response
        result = self.client.b2b_order_booking_form(data=self.request)

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, B2BHotelOrderBookingFormData)

    @patch("papi_sdk.APIv3._post_request")
    def test_affiliate_ok(self, m_post):
        m_post.return_value = affiliate_order_booking_form_response
        result = self.client.affiliate_order_booking_form(data=self.request)

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, AffiliateHotelOrderBookingFormData)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.b2b_order_booking_form(data=OrderBookingFormRequest())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.b2b_order_booking_form()

    @patch("papi_sdk.APIv3._post_request")
    def test_double_booking_form(self, m_post):
        m_post.return_value = order_booking_form_error
        result = self.client.b2b_order_booking_form(data=self.request)

        self.assertEqual(result.status.value, self.status_error)

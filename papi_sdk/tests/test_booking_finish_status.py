from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.order_booking_finish_status import (
    HotelOrderBookingFinishStatusData,
    HotelOrderBookingFinishStatusRequest,
)
from papi_sdk.tests.mocked_data.order_booking_finish_status import (
    order_booking_finish_status_response,
    order_booking_finish_status_response_error,
)
from papi_sdk.tests.test_base import BaseTest


class TestOrderBookingFinishStatus(BaseTest):
    @patch("papi_sdk.APIv3._post_request")
    def test_ok(self, m_post):
        m_post.return_value = order_booking_finish_status_response
        result = self.client.order_booking_finish_status(
            data=HotelOrderBookingFinishStatusRequest(partner_order_id="test")
        )

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, HotelOrderBookingFinishStatusData)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.order_booking_finish_status(
                data=HotelOrderBookingFinishStatusRequest()
            )

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.order_booking_finish_status()

    @patch("papi_sdk.APIv3._post_request")
    def test_error_hotel_not_found(self, m_post):
        m_post.return_value = order_booking_finish_status_response_error
        result = self.client.order_booking_finish_status(
            data=HotelOrderBookingFinishStatusRequest(partner_order_id="not_found")
        )

        self.assertEqual(result.status.value, self.status_error)

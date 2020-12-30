from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.order_booking_finish.b2b import (
    B2BHotelOrderBookingFinishPartner,
    B2BHotelOrderBookingFinishRequest,
)
from papi_sdk.models.order_booking_finish.base import (
    HotelOrderBookingFinishGuest,
    HotelOrderBookingFinishPaymentType,
    HotelOrderBookingFinishRoom,
    HotelOrderBookingFinishUser,
)
from papi_sdk.tests.mocked_data.booking_order_finish import (
    booking_order_finish_book_hash_not_found_error,
    booking_order_finish_response,
)
from papi_sdk.tests.test_base import BaseTest


class TestOrderBookingForm(BaseTest):
    request = B2BHotelOrderBookingFinishRequest(
        **{
            "user": HotelOrderBookingFinishUser(
                **{
                    "email": "foo@bar.com",
                    "comment": "comment",
                    "phone": "74950000000",
                }
            ),
            "partner": B2BHotelOrderBookingFinishPartner(
                **{
                    "partner_order_id": "test_02",
                    "comment": "upsell comment",
                    "amount_sell_b2b2c": "10000",
                }
            ),
            "language": "en",
            "ignore_group_booking_error": True,
            "rooms": [
                HotelOrderBookingFinishRoom(
                    **{
                        "guests": [
                            HotelOrderBookingFinishGuest(
                                **{"first_name": "One", "last_name": "Two"}
                            )
                        ]
                    }
                )
            ],
            "payment_type": HotelOrderBookingFinishPaymentType(
                **{"type": "deposit", "amount": "18.9", "currency_code": "PLN"}
            ),
        }
    )

    @patch("papi_sdk.APIv3._post_request")
    def test_b2b_ok(self, m_post):
        m_post.return_value = booking_order_finish_response
        result = self.client.b2b_order_booking_finish(data=self.request)

        self.assertEqual(result.status.value, self.status_ok)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.b2b_order_booking_finish(
                data=B2BHotelOrderBookingFinishRequest()
            )

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.b2b_order_booking_finish()

    @patch("papi_sdk.APIv3._post_request")
    def test_hash_not_found_error(self, m_post):
        m_post.return_value = booking_order_finish_book_hash_not_found_error
        result = self.client.b2b_order_booking_finish(data=self.request)

        self.assertEqual(result.status.value, self.status_error)

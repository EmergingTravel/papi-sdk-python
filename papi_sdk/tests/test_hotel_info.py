from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.hotel_info import HotelInfoData, HotelInfoRequest
from papi_sdk.tests.mocked_data.hotel_info import (
    hotel_info_data,
    hotel_info_error_response,
)
from papi_sdk.tests.test_base import BaseTest


class TestHotelInfo(BaseTest):
    @patch("papi_sdk.APIv3._post_request")
    def test_ok(self, m_post):
        m_post.return_value = hotel_info_data
        result = self.client.get_hotel_info(
            data=HotelInfoRequest(language="ru", id="test_hotel")
        )

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, HotelInfoData)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.get_hotel_info(data=HotelInfoRequest())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.get_hotel_info()

    @patch("papi_sdk.APIv3._post_request")
    def test_error_hotel_not_found(self, m_post):
        m_post.return_value = hotel_info_error_response
        result = self.client.get_hotel_info(
            data=HotelInfoRequest(language="en", id="not_exist")
        )

        self.assertEqual(result.status.value, self.status_error)

from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.hotel_info_dump import HotelInfoDumpData, HotelInfoDumpRequest
from papi_sdk.tests.mocked_data.hotel_info_dump import (
    hotel_info_dump_error_response,
    hotel_info_dump_response,
)
from papi_sdk.tests.test_base import BaseTest


class TestHotelInfoDump(BaseTest):
    @patch("papi_sdk.APIv3._post_request")
    def test_ok(self, m_post):
        m_post.return_value = hotel_info_dump_response
        result = self.client.get_hotel_info_dump(
            data=HotelInfoDumpRequest(language="ru")
        )

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, HotelInfoDumpData)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.get_hotel_info_dump(data=HotelInfoDumpRequest())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.get_hotel_info_dump()

    @patch("papi_sdk.APIv3._post_request")
    def test_not_valid_language(self, m_post):
        m_post.return_value = hotel_info_dump_error_response
        result = self.client.get_hotel_info_dump(
            data=HotelInfoDumpRequest(language="not_valid")
        )

        self.assertEqual(result.status.value, self.status_error)

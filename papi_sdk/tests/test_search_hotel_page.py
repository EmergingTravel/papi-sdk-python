from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.search.base_request import ECLC, GuestsGroup, Upsells
from papi_sdk.models.search.hotelpage.affiliate import (
    AffiliateHotelPageRequest,
    HotelPageAffiliateSearchData,
)
from papi_sdk.models.search.hotelpage.b2b import (
    B2BHotelPageRequest,
    HotelPageB2BSearchData,
)
from papi_sdk.tests.mocked_data.search_hotel_page import (
    affiliate_hotel_page_response,
    b2b_hotel_page_response,
)
from papi_sdk.tests.test_base import BaseTest


class TestSearchHotelPage(BaseTest):
    b2b_request = B2BHotelPageRequest(
        **{
            "id": "test_hotel",
            "checkin": "2020-08-05",
            "checkout": "2020-08-06",
            "residency": "ru",
            "language": "ru",
            "guests": [GuestsGroup(**{"adults": 1, "children": []})],
            "upsells": Upsells(
                **{
                    "early_checkin": ECLC(**{"time": "2020-08-05T10:00:00"}),
                    "late_checkout": ECLC(**{"time": "2020-08-06T15:00:00"}),
                    "only_eclc": True,
                }
            ),
        }
    )

    affiliate_request = AffiliateHotelPageRequest(
        **{
            "id": "test_hotel",
            "checkin": "2020-08-05",
            "checkout": "2020-08-06",
            "residency": "ru",
            "language": "ru",
            "guests": [GuestsGroup(**{"adults": 1, "children": []})],
        }
    )

    @patch("papi_sdk.APIv3._post_request")
    def test_b2b_ok(self, m_post):
        m_post.return_value = b2b_hotel_page_response
        result = self.client.b2b_search_hotel_page(data=self.b2b_request)

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, HotelPageB2BSearchData)

    @patch("papi_sdk.APIv3._post_request")
    def test_affiliate_ok(self, m_post):
        m_post.return_value = affiliate_hotel_page_response
        result = self.client.affiliate_search_hotel_page(data=self.affiliate_request)

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, HotelPageAffiliateSearchData)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.b2b_search_hotel_page(data=B2BHotelPageRequest())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.b2b_search_hotel_page()

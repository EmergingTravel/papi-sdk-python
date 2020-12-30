from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.search.base_request import ECLC, GuestsGroup, Upsells
from papi_sdk.models.search.region.affiliate import (
    AffiliateRegionRequest,
    RegionAffiliateSearchData,
)
from papi_sdk.models.search.region.b2b import B2BRegionRequest, RegionB2BSearchData
from papi_sdk.tests.mocked_data.search_region import (
    affiliate_region_response,
    b2b_region_response,
)
from papi_sdk.tests.test_base import BaseTest


class TestSearchHotelPage(BaseTest):
    b2b_request = B2BRegionRequest(
        **{
            "region_id": 3,
            "checkin": "2020-08-05",
            "checkout": "2020-08-06",
            "residency": "ru",
            "language": "ru",
            "guests": [GuestsGroup(**{"adults": 4, "children": []})],
            "upsells": Upsells(
                **{
                    "early_checkin": ECLC(**{"time": "2020-08-05T10:00:00"}),
                    "late_checkout": ECLC(**{"time": "2020-08-06T15:00:00"}),
                    "only_eclc": True,
                }
            ),
        }
    )

    affiliate_request = AffiliateRegionRequest(
        **{
            "region_id": 3,
            "checkin": "2020-08-05",
            "checkout": "2020-08-06",
            "residency": "ru",
            "language": "ru",
            "guests": [GuestsGroup(**{"adults": 4, "children": []})],
        }
    )

    @patch("papi_sdk.APIv3._post_request")
    def test_b2b_ok(self, m_post):
        m_post.return_value = b2b_region_response
        result = self.client.b2b_search_region(data=self.b2b_request)

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, RegionB2BSearchData)

    @patch("papi_sdk.APIv3._post_request")
    def test_affiliate_ok(self, m_post):
        m_post.return_value = affiliate_region_response
        result = self.client.affiliate_search_region(data=self.affiliate_request)

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, RegionAffiliateSearchData)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.b2b_search_hotel_page(data=B2BRegionRequest())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.b2b_search_hotel_page()

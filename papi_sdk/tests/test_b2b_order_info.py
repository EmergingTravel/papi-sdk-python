from unittest.mock import patch

from pydantic import ValidationError

from papi_sdk.models.order_info.b2b import (
    B2BHotelOrderInfoData,
    B2BHotelOrderInfoDataRequest,
)
from papi_sdk.models.order_info.base import (
    HotelOrdering,
    OrderingBy,
    OrderingType,
    Pagination,
)
from papi_sdk.tests.mocked_data.b2b_order_info import b2b_order_info_response
from papi_sdk.tests.test_base import BaseTest


class TestB2BOrderInfo(BaseTest):
    def _create_request(self):
        ordering = HotelOrdering(
            ordering_type=OrderingType.ASC,
            ordering_by=OrderingBy.FIELD_CHECKIN_AT,
        )
        paginator = Pagination(page_number=1, page_size=1)
        return B2BHotelOrderInfoDataRequest(ordering=ordering, pagination=paginator)

    @patch("papi_sdk.APIv3._post_request")
    def test_ok(self, m_post):
        m_post.return_value = b2b_order_info_response
        result = self.client.b2b_order_info(data=self._create_request())

        self.assertEqual(result.status.value, self.status_ok)
        self.assertIsInstance(result.data, B2BHotelOrderInfoData)

    def test_validation_error(self):
        with self.assertRaises(ValidationError):
            self.client.b2b_order_info(data=B2BHotelOrderInfoDataRequest())

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.client.b2b_order_info()

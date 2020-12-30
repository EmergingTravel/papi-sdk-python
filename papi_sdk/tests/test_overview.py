from unittest.mock import patch

from papi_sdk.models.overview import OverviewData
from papi_sdk.tests.mocked_data.overview import overview_response
from papi_sdk.tests.test_base import BaseTest


class TestOverview(BaseTest):
    @patch("papi_sdk.APIv3._get_request")
    def test_ok(self, m_get):
        m_get.return_value = overview_response
        result = self.client.overview()

        self.assertEqual(result.status.value, self.status_ok)
        for overview_data in result.data:
            self.assertIsInstance(overview_data, OverviewData)

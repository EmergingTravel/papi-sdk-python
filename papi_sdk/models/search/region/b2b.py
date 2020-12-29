from typing import Optional

from papi_sdk.models.search.base_b2b_response import (
    BaseB2BSearchData,
    BaseB2BSearchResponse,
)
from papi_sdk.models.search.base_request import BaseB2BRequest


class B2BRegionRequest(BaseB2BRequest):
    region_id: int


class RegionB2BSearchData(BaseB2BSearchData):
    total_hotels: int


class B2BRegionResponse(BaseB2BSearchResponse):
    data: Optional[RegionB2BSearchData]

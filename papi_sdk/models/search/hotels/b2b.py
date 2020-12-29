from typing import List, Optional

from papi_sdk.models.search.base_b2b_response import (
    BaseB2BSearchData,
    BaseB2BSearchResponse,
)
from papi_sdk.models.search.base_request import BaseB2BRequest


class B2BHotelsRequest(BaseB2BRequest):
    ids: List[str]


class HotelsB2BSearchData(BaseB2BSearchData):
    total_hotels: int


class B2BHotelsResponse(BaseB2BSearchResponse):
    data: Optional[HotelsB2BSearchData]

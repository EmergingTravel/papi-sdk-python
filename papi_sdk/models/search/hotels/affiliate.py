from typing import List, Optional

from papi_sdk.models.search.base_affiliate_response import (
    BaseAffiliateSearchData,
    BaseAffiliateSearchResponse,
)
from papi_sdk.models.search.base_request import BaseAffiliateRequest


class AffiliateHotelsRequest(BaseAffiliateRequest):
    ids: List[str]


class HotelsAffiliateSearchData(BaseAffiliateSearchData):
    total_hotels: int


class AffiliateHotelsResponse(BaseAffiliateSearchResponse):
    data: Optional[HotelsAffiliateSearchData]

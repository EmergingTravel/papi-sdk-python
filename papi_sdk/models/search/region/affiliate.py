from typing import Optional

from papi_sdk.models.search.base_affiliate_response import (
    BaseAffiliateSearchData,
    BaseAffiliateSearchResponse,
)
from papi_sdk.models.search.base_request import BaseAffiliateRequest


class AffiliateRegionRequest(BaseAffiliateRequest):
    region_id: int


class RegionAffiliateSearchData(BaseAffiliateSearchData):
    total_hotels: int


class AffiliateRegionResponse(BaseAffiliateSearchResponse):
    data: Optional[RegionAffiliateSearchData]

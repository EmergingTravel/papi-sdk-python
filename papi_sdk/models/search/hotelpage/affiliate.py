from typing import List, Optional

from papi_sdk.models.search.base_affiliate_response import (
    BaseAffiliateSearchData,
    BaseAffiliateSearchResponse,
    BaseHotel,
    BaseRate,
)
from papi_sdk.models.search.base_request import BaseAffiliateRequest


class AffiliateHotelPageRequest(BaseAffiliateRequest):
    id: str


class Rate(BaseRate):
    book_hash: str


class Hotel(BaseHotel):
    rates: List[Rate]


class HotelPageAffiliateSearchData(BaseAffiliateSearchData):
    hotels: List[Hotel]


class AffiliateHotelPageResponse(BaseAffiliateSearchResponse):
    data: Optional[HotelPageAffiliateSearchData]

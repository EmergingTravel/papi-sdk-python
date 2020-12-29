from typing import List, Optional

from papi_sdk.models.search.base_b2b_response import (
    BaseB2BSearchData,
    BaseB2BSearchResponse,
    BaseHotel,
    BaseRate,
)
from papi_sdk.models.search.base_request import BaseB2BRequest


class B2BHotelPageRequest(BaseB2BRequest):
    id: str


class Rate(BaseRate):
    book_hash: str


class Hotel(BaseHotel):
    rates: List[Rate]


class HotelPageB2BSearchData(BaseB2BSearchData):
    hotels: List[Hotel]


class B2BHotelPageResponse(BaseB2BSearchResponse):
    data: Optional[HotelPageB2BSearchData]

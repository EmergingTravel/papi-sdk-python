from typing import List, Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse
from papi_sdk.models.order_info.base import (
    BaseHotelOrderData,
    BaseHotelOrderInfoDataRequest,
    BaseHotelOrderInfoDataResponse,
)


# request
class AffiliateHotelSearchData(BaseModel):
    source: Optional[str]


class AffiliateHotelOrderInfoDataRequest(BaseHotelOrderInfoDataRequest):
    search: Optional[AffiliateHotelSearchData]


# response
class AffiliateHotelOrderData(BaseHotelOrderData):
    pass


class AffiliateHotelOrderInfoData(BaseHotelOrderInfoDataResponse):
    orders: List[AffiliateHotelOrderData]


class AffiliateHotelOrderInfoDataResponse(BaseResponse):
    data: Optional[AffiliateHotelOrderInfoData]

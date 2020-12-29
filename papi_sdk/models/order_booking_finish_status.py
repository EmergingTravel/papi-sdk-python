from typing import Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse


class HotelOrderBookingFinishStatusRequest(BaseModel):
    partner_order_id: str


class Data3DS(BaseModel):
    action_url: str
    method: str
    data: Optional[dict]


class HotelOrderBookingFinishStatusData(BaseModel):
    data_3ds: Optional[Data3DS]
    partner_order_id: str
    percent: int


class HotelOrderBookingFinishStatusResponse(BaseResponse):
    data: Optional[HotelOrderBookingFinishStatusData]

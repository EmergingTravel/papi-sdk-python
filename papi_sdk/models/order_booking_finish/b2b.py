from typing import Optional

from pydantic import BaseModel

from papi_sdk.models.order_booking_finish.base import (
    BaseHotelOrderBookingFinishPartner,
    BaseHotelOrderBookingFinishRequest,
)


class HotelOrderBookingFinishUpsellAttributes(BaseModel):
    checkin_datetime: Optional[str]
    checkout_datetime: Optional[str]


class HotelOrderBookingFinishUpsellData(BaseModel):
    attributes: Optional[HotelOrderBookingFinishUpsellAttributes]
    name: Optional[str]
    rule_id: Optional[int]
    uid: Optional[str]


class B2BHotelOrderBookingFinishPartner(BaseHotelOrderBookingFinishPartner):
    comment: Optional[str]


class B2BHotelOrderBookingFinishRequest(BaseHotelOrderBookingFinishRequest):
    upsell_data: Optional[HotelOrderBookingFinishUpsellData]
    is_vip: Optional[bool]
    partner: B2BHotelOrderBookingFinishPartner

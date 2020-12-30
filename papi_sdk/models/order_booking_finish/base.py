from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse


class HotelOrderBookingFinishPaymentType(BaseModel):
    amount: Decimal
    currency_code: str
    type: str
    init_uuid: Optional[str]
    pay_uuid: Optional[str]


class HotelOrderBookingFinishGuest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    is_child: Optional[bool]


class HotelOrderBookingFinishRoom(BaseModel):
    guests: List[HotelOrderBookingFinishGuest]


class HotelOrderBookingFinishUser(BaseModel):
    comment: Optional[str]
    email: Optional[str]
    phone: Optional[str]


class BaseHotelOrderBookingFinishPartner(BaseModel):
    amount_sell_b2b2c: Optional[str]
    partner_order_id: Optional[str]


class BaseHotelOrderBookingFinishRequest(BaseModel):
    arrival_datetime: Optional[datetime]
    book_timeout: Optional[int]
    ignore_group_booking_error: Optional[bool]
    language: str
    payment_type: HotelOrderBookingFinishPaymentType
    return_path: Optional[str]
    rooms: List[HotelOrderBookingFinishRoom]
    user: HotelOrderBookingFinishUser


class HotelOrderBookingFinishData(BaseModel):
    order_token: str


class HotelOrderBookingFinishResponse(BaseResponse):
    data: Optional[HotelOrderBookingFinishData]

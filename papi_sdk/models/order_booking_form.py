from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse


class OrderBookingFormRequest(BaseModel):
    book_hash: str
    language: str
    partner_order_id: str
    user_ip: str


class HotelOrderBookingFormUpsellPriceData(BaseModel):
    amount: Decimal
    currency_code: str


class HotelOrderBookingFormPaymentType(BaseModel):
    amount: Decimal
    currency_code: str
    is_need_credit_card_data: bool
    is_need_cvc: bool
    type: str


class BaseHotelOrderBookingFormData(BaseModel):
    order_id: int
    partner_order_id: str
    payment_types: List[HotelOrderBookingFormPaymentType]
    item_id: int


class HotelOrderBookingFormUpsellData(BaseModel):
    charge_price: HotelOrderBookingFormUpsellPriceData
    name: str
    rule_id: int
    uid: Optional[str]
    data: Optional[str]


class B2BHotelOrderBookingFormData(BaseHotelOrderBookingFormData):
    upsell_data: List[HotelOrderBookingFormUpsellData]


class AffiliateHotelOrderBookingFormData(BaseHotelOrderBookingFormData):
    pass


class B2BHotelOrderBookingFormResponse(BaseResponse):
    data: Optional[B2BHotelOrderBookingFormData]


class AffiliateHotelOrderBookingFormResponse(BaseResponse):
    data: Optional[AffiliateHotelOrderBookingFormData]

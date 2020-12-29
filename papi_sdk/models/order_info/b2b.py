from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse
from papi_sdk.models.order_info.base import (
    AmountOfMoney,
    BaseHotelOrderData,
    BaseHotelOrderInfoDataRequest,
    BaseHotelOrderInfoDataResponse,
    DateRange,
)


# request
class B2BHotelSearchData(BaseModel):
    paid_at: Optional[DateRange]
    payment_due: Optional[DateRange]
    payment_pending: Optional[DateRange]
    source: Optional[str]


class B2BHotelOrderInfoDataRequest(BaseHotelOrderInfoDataRequest):
    language: Optional[str]
    search: Optional[B2BHotelSearchData]


# response
class HotelOrderMetaData(BaseModel):
    voucher_order_comment: Optional[str]


class PaymentData(BaseModel):
    invoice_id: Optional[int]
    paid_at: Optional[date]
    payment_by: Optional[str]
    payment_due: Optional[str]
    payment_pending: date
    payment_type: str


class HotelOrderUpsellData(BaseModel):
    amount_payable: Optional[AmountOfMoney]
    amount_payable_vat: Optional[AmountOfMoney]
    amount_refunded: Optional[AmountOfMoney]
    amount_sell: Optional[AmountOfMoney]
    amount_sell_b2b2c: Optional[AmountOfMoney]
    cancelled_at: Optional[str]
    created_at: Optional[datetime]
    free_cancellation_before: Optional[str]
    info: Optional[dict]
    order_id: Optional[int]
    order_type: Optional[str]
    payment_data: Optional[PaymentData]
    status: Optional[str]
    type: Optional[str]


class UserData(BaseModel):
    email: str


class B2bHotelOrderData(BaseHotelOrderData):
    amount_payable_with_upsells: AmountOfMoney
    invoice_id: Optional[str]
    is_checked: bool
    meta_data: HotelOrderMetaData
    payment_data: PaymentData
    upsells: HotelOrderUpsellData
    user_data: UserData


class B2BHotelOrderInfoData(BaseHotelOrderInfoDataResponse):
    orders: List[B2bHotelOrderData]


class B2BHotelOrderInfoDataResponse(BaseResponse):
    data: Optional[B2BHotelOrderInfoData]

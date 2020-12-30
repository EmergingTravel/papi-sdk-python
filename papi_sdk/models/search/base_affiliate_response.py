from datetime import time
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, Field

from papi_sdk.models.base import BaseResponse


class CancellationPolicy(BaseModel):
    start_at: Optional[str]
    end_at: Optional[str]
    amount_charge: Optional[Decimal]
    amount_show: Optional[Decimal]


class CancellationPenalty(BaseModel):
    policies: List[CancellationPolicy]
    free_cancellation_before: Optional[str]


class Tax(BaseModel):
    name: str
    included_by_supplier: bool
    amount: Decimal
    currency_code: str


class TaxData(BaseModel):
    taxes: Optional[List[Tax]]


class PaymentType(BaseModel):
    amount: Decimal
    show_amount: Decimal
    currency_code: str
    show_currency_code: str
    by: Optional[str]
    is_need_credit_card_data: bool
    is_need_cvc: bool
    type: str
    tax_data: TaxData
    cancellation_penalties: CancellationPenalty


class PaymentOptions(BaseModel):
    payment_types: List[PaymentType]


class RgExt(BaseModel):
    rg_class: Optional[int] = Field(None, alias="class")
    quality: Optional[int]
    sex: Optional[int]
    bathroom: Optional[int]
    bedding: Optional[int]
    family: Optional[int]
    capacity: Optional[int]
    club: Optional[int]


class Deposit(BaseModel):
    amount: Decimal
    currency_code: str
    is_refundable: bool


class NoShow(BaseModel):
    amount: Decimal
    currency_code: str
    from_time: time


class BaseRate(BaseModel):
    daily_prices: List[str]
    meal: str
    payment_options: PaymentOptions
    rg_ext: Optional[RgExt]
    room_name: str
    serp_filters: List[str]
    sell_price_limits: Optional[str]
    allotment: Optional[int]
    amenities_data: List[str]
    any_residency: bool
    deposit: Optional[Deposit]
    no_show: Optional[NoShow]


class BaseHotel(BaseModel):
    id: str
    rates: List[BaseRate]


class BaseAffiliateSearchData(BaseModel):
    hotels: List[BaseHotel]


class BaseAffiliateSearchResponse(BaseResponse):
    data: Optional[BaseAffiliateSearchData]

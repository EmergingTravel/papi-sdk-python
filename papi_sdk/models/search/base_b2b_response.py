from datetime import time
from decimal import Decimal
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from papi_sdk.models.base import BaseResponse


class CommissionInfoItem(BaseModel):
    amount_gross: Decimal
    amount_net: Decimal
    amount_commission: Decimal


class CommissionInfo(BaseModel):
    show: CommissionInfoItem
    charge: CommissionInfoItem


class CancellationPolicy(BaseModel):
    start_at: Optional[str]
    end_at: Optional[str]
    amount_charge: Optional[Decimal]
    amount_show: Optional[Decimal]
    commission_info: Optional[CommissionInfo]


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


class VatData(BaseModel):
    included: bool
    value: str


class ECLCPerk(BaseModel):
    charge_price: Decimal
    show_price: Decimal
    commission_info: CommissionInfo
    time: str


class Perks(BaseModel):
    early_checkin: List[ECLCPerk]
    late_checkout: List[ECLCPerk]


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
    vat_data: VatData
    perks: Union[Perks, dict]
    commission_info: CommissionInfo


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


class SellPriceLimits(BaseModel):
    min_price: Decimal
    max_price: Decimal


class BarRatePriceData(BaseModel):
    amount: Decimal
    currency_code: str


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
    sell_price_limits: Optional[SellPriceLimits]
    bar_rate_price_data: Optional[BarRatePriceData]


class HotelBarPriceData(BaseModel):
    price: str
    currency: str


class RoomGroupsBarPriceData(BaseModel):
    rg_ext: RgExt
    price: str
    currency: str


class BarPriceData(BaseModel):
    hotel: Optional[HotelBarPriceData]
    room_groups: List[RoomGroupsBarPriceData]


class BaseHotel(BaseModel):
    id: str
    rates: List[BaseRate]
    bar_price_data: Optional[BarPriceData]


class BaseB2BSearchData(BaseModel):
    hotels: List[BaseHotel]


class BaseB2BSearchResponse(BaseResponse):
    data: Optional[BaseB2BSearchData]

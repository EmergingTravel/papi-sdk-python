from datetime import date
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class OrderingType(str, Enum):
    ASC = "asc"
    DESC = "desc"


class OrderingBy(str, Enum):
    FIELD_CANCELLED_AT = "cancelled_at"
    FIELD_CHECKIN_AT = "checkin_at"
    FIELD_CHECKOUT_AT = "checkout_at"
    FIELD_CREATED_AT = "created_at"
    FIELD_FREE_CANCELLATION_BEFORE = "free_cancellation_before"
    FIELD_PAID_AT = "paid_at"
    FIELD_PAYMENT_DUE = "payment_due"
    FIELD_PAYMENT_PENDING = "payment_pending"


# request
class HotelOrdering(BaseModel):
    ordering_type: OrderingType
    ordering_by: OrderingBy


class Pagination(BaseModel):
    page_number: int
    page_size: int


class BaseHotelOrderInfoDataRequest(BaseModel):
    ordering: HotelOrdering
    pagination: Pagination


# response
class AmountOfMoney(BaseModel):
    amount: Decimal
    currency_code: str


class DateRange(BaseModel):
    from_date: Optional[date]
    to_date: Optional[date]


class CancellationPolicyData(BaseModel):
    end_at: Optional[str]
    penalty: Optional[AmountOfMoney]
    start_at: Optional[str]


class CancellationInfoData(BaseModel):
    free_cancellation_before: Optional[str]
    policies: Optional[List[CancellationPolicyData]]


class HotelData(BaseModel):
    id: str
    order_id: Optional[str]


class PartnerData(BaseModel):
    order_comment: Optional[str]
    order_id: str


class GuestData(BaseModel):
    first_name: str
    last_name: str
    is_child: Optional[bool]
    age: Optional[int]


class RoomGuestData(BaseModel):
    adults_number: int
    children_number: int
    guests: List[GuestData]


class RoomData(BaseModel):
    bedding_name: List[str]
    guest_data: RoomGuestData
    meal_name: str
    room_idx: int
    room_name: str


class SupplierData(BaseModel):
    name: Optional[str]
    order_id: Optional[str]


class TaxData(BaseModel):
    amount_tax: Optional[AmountOfMoney]
    is_included: Optional[bool]
    name: Optional[str]


class BaseHotelOrderData(BaseModel):
    agreement_number: Optional[str]
    amount_payable: AmountOfMoney
    amount_payable_vat: Optional[AmountOfMoney]
    amount_refunded: Optional[AmountOfMoney]
    amount_sell: AmountOfMoney
    amount_sell_b2b2c: Optional[AmountOfMoney]
    api_auth_key_id: Optional[int]
    cancellation_info: Optional[CancellationInfoData]
    cancelled_at: Optional[str]
    checkin_at: date
    checkout_at: str
    contract_slug: str
    created_at: str
    hotel_data: HotelData
    nights: int
    order_id: int
    order_type: str
    partner_data: PartnerData
    roomnights: int
    rooms_data: List[RoomData]
    source: str
    status: str
    supplier_data: SupplierData
    taxes: Optional[List[TaxData]]
    total_vat: Optional[AmountOfMoney]


class BaseHotelOrderInfoDataResponse(BaseModel):
    current_page_number: int
    total_orders: int
    total_pages: int

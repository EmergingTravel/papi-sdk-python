from datetime import time
from typing import List, Optional

from pydantic import BaseModel, Field

from papi_sdk.models.base import BaseResponse


class HotelInfoRequest(BaseModel):
    id: str
    language: str


class AmenityGroup(BaseModel):
    amenities: List[str]
    group_name: Optional[str]


class DescriptionItem(BaseModel):
    paragraphs: List[str]
    title: Optional[str]


class PolicyItem(BaseModel):
    paragraphs: List[str]
    title: Optional[str]


class Region(BaseModel):
    country_code: str
    iata: Optional[str]
    id: int
    name: Optional[str]
    type: str


class RgExt(BaseModel):
    rg_class: Optional[int] = Field(None, alias="class")
    quality: Optional[int]
    sex: Optional[int]
    bathroom: Optional[int]
    bedding: Optional[int]
    family: Optional[int]
    capacity: Optional[int]
    club: Optional[int]


class RoomGroup(BaseModel):
    images: List[str]
    name: str
    room_amenities: List[str]
    room_group_id: Optional[int]
    rg_ext: RgExt


class Visa(BaseModel):
    visa_support: Optional[str]


class Shuttle(BaseModel):
    currency: Optional[str]
    inclusion: Optional[str]
    shuttle_type: Optional[str]
    price: Optional[float]
    destination_type: Optional[str]


class Pets(BaseModel):
    currency: Optional[str]
    inclusion: Optional[str]
    pets_type: Optional[str]
    price: Optional[float]
    price_unit: Optional[str]


class Parking(BaseModel):
    currency: Optional[str]
    inclusion: Optional[str]
    territory_type: Optional[str]
    price: Optional[float]
    price_unit: Optional[str]


class NoShow(BaseModel):
    availability: Optional[str]
    day_period: Optional[str]
    time: Optional[str]


class Meal(BaseModel):
    currency: Optional[str]
    inclusion: Optional[str]
    meal_type: Optional[str]
    price: Optional[float]


class Internet(BaseModel):
    currency: Optional[str]
    inclusion: Optional[str]
    internet_type: Optional[str]
    price: Optional[float]
    price_unit: Optional[str]
    work_area: Optional[str]


class ExtraBed(BaseModel):
    amount: Optional[int]
    currency: Optional[str]
    inclusion: Optional[str]
    price: Optional[float]
    price_unit: Optional[str]


class Deposit(BaseModel):
    availability: Optional[str]
    currency: Optional[str]
    deposit_type: Optional[str]
    payment_type: Optional[str]
    price: Optional[float]
    price_unit: Optional[str]
    pricing_method: Optional[str]


class Cradle(BaseModel):
    amount: Optional[int]
    currency: Optional[str]
    inclusion: Optional[str]
    price: Optional[float]
    price_unit: Optional[str]


class ChildrenMeal(BaseModel):
    age_end: Optional[int]
    age_start: Optional[int]
    currency: Optional[str]
    inclusion: Optional[str]
    meal_type: Optional[str]
    price: Optional[float]


class Children(BaseModel):
    age_end: Optional[int]
    age_start: Optional[int]
    currency: Optional[str]
    extra_bed: Optional[str]
    price: Optional[float]


class CheckinCheckout(BaseModel):
    currency: Optional[str]
    inclusion: Optional[str]
    price: Optional[float]


class AddFee(BaseModel):
    currency: Optional[str]
    fee_type: Optional[str]
    price: Optional[float]
    price_unit: Optional[str]


class MetapolicyStruct(BaseModel):
    internet: List[Internet]
    add_fee: List[AddFee]
    check_in_check_out: Optional[List[CheckinCheckout]]
    children: List[Children]
    children_meal: List[ChildrenMeal]
    cradle: Optional[List[Cradle]]
    deposit: List[Deposit]
    extra_bed: List[ExtraBed]
    meal: List[Meal]
    no_show: Optional[NoShow]
    parking: List[Parking]
    pets: List[Pets]
    shuttle: List[Shuttle]
    visa: Optional[Visa]


class HotelInfoData(BaseModel):
    address: str
    amenity_groups: List[AmenityGroup]
    check_in_time: time
    check_out_time: time
    description_struct: List[DescriptionItem]
    email: Optional[str]
    id: str
    images: List[str]
    kind: str
    latitude: float
    longitude: float
    name: str
    metapolicy_struct: MetapolicyStruct
    phone: Optional[str]
    policy_struct: List[PolicyItem]
    postal_code: Optional[str]
    region: Region
    room_groups: List[RoomGroup]
    star_rating: int
    serp_filters: List[str]
    is_closed: bool


class HotelInfoResponse(BaseResponse):
    data: Optional[HotelInfoData]

from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class GuestsGroup(BaseModel):
    adults: int
    children: Optional[List[int]]


class BaseRequest(BaseModel):
    checkin: date
    checkout: date
    currency: Optional[str]
    residency: Optional[str]
    timeout: Optional[int]
    language: Optional[str]
    guests: List[GuestsGroup]


class ECLC(BaseModel):
    time: str


class Upsells(BaseModel):
    early_checkin: Optional[ECLC]
    late_checkout: Optional[ECLC]
    only_eclc: Optional[bool]


class BaseB2BRequest(BaseRequest):
    upsells: Optional[Upsells]


class BaseAffiliateRequest(BaseRequest):
    pass

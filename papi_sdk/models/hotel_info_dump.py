from typing import Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse


class HotelInfoDumpRequest(BaseModel):
    language: str


class HotelInfoDumpData(BaseModel):
    url: str


class HotelInfoDumpResponse(BaseResponse):
    data: Optional[HotelInfoDumpData]

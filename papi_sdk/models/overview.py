from typing import List, Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse


class OverviewData(BaseModel):
    endpoint: str
    is_active: bool
    is_debug_mode: bool
    is_limited: bool
    requests_number: int
    seconds_number: int


class OverviewResponse(BaseResponse):
    data: Optional[List[OverviewData]]

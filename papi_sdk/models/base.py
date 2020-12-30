from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Status(str, Enum):
    STATUS_OK = "ok"
    STATUS_ERROR = "error"


class BaseResponse(BaseModel):
    debug: Optional[dict]
    error: Optional[str]
    status: Optional[Status]

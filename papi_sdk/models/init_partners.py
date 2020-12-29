from typing import Optional

from pydantic import BaseModel

from papi_sdk.models.base import BaseResponse


class CreditCardDataCore(BaseModel):
    card_number: str
    card_holder: str
    month: str
    year: str


class InitPartnerRequest(BaseModel):
    object_id: str
    pay_uuid: str
    init_uuid: str
    user_first_name: str
    user_last_name: str
    cvc: Optional[str]
    is_cvc_required: bool
    credit_card_data_core: CreditCardDataCore


class InitPartnerResponse(BaseResponse):
    pass

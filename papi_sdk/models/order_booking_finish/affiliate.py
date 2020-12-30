from papi_sdk.models.order_booking_finish.base import (
    BaseHotelOrderBookingFinishPartner,
    BaseHotelOrderBookingFinishRequest,
)


class AffiliateHotelOrderBookingFinishPartner(BaseHotelOrderBookingFinishPartner):
    pass


class AffiliateHotelOrderBookingFinishRequest(BaseHotelOrderBookingFinishRequest):
    partner: AffiliateHotelOrderBookingFinishPartner

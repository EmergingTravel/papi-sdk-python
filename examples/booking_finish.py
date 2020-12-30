from papi_sdk import APIv3
from papi_sdk.models.order_booking_finish.b2b import (
    B2BHotelOrderBookingFinishPartner,
    B2BHotelOrderBookingFinishRequest,
)
from papi_sdk.models.order_booking_finish.base import (
    HotelOrderBookingFinishGuest,
    HotelOrderBookingFinishPaymentType,
    HotelOrderBookingFinishResponse,
    HotelOrderBookingFinishRoom,
    HotelOrderBookingFinishUser,
)


def make_booking_finish(
    client: APIv3,
    email: str,
    phone: str,
    order_id: str,
    language: str,
    guest_first_name: str,
    guest_last_name: str,
    pt_type: str,
    pt_amount: str,
    pt_currency_code: str,
) -> HotelOrderBookingFinishResponse:
    """
    The full documentation is available in https://docs.emergingtravel.com/?version=latest#b79e9280-16da-4d51-b500-7f1c3bfd0f78
    """
    user = HotelOrderBookingFinishUser(
        email=email,
        phone=phone,
    )
    rooms = [
        HotelOrderBookingFinishRoom(
            guests=[
                HotelOrderBookingFinishGuest(
                    first_name=guest_first_name,
                    last_name=guest_last_name,
                )
            ]
        )
    ]
    payment_type = HotelOrderBookingFinishPaymentType(
        type=pt_type,
        amount=pt_amount,
        currency_code=pt_currency_code,
    )
    return client.b2b_order_booking_finish(
        data=B2BHotelOrderBookingFinishRequest(
            user=user,
            partner=B2BHotelOrderBookingFinishPartner(partner_order_id=order_id),
            language=language,
            rooms=rooms,
            payment_type=payment_type,
        )
    )


if __name__ == "__main__":
    papi = APIv3(key="your_key")
    result = make_booking_finish(
        client=papi,
        email="your_email_address",
        phone="your_phone",
        order_id="your_order_id",
        language="ru",
        guest_first_name="John",
        guest_last_name="Johnson",
        pt_type="payment_type_from_booking_form",
        pt_amount="payment_amount_from_booking_form",
        pt_currency_code="payment_currency_code_from_booking_form",
    )
    print(f"booking finish status is {result.status}")

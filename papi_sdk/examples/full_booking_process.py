from datetime import datetime, timedelta

from papi_sdk import APIv3
from papi_sdk.examples.booking_finish import make_booking_finish
from papi_sdk.examples.booking_form import make_booking_form
from papi_sdk.examples.search_hotelpage import get_hotel_page

if __name__ == "__main__":
    papi = APIv3(key="your_key")

    # The first step - we need to get hotel page data
    hp = get_hotel_page(
        client=papi,
        hotel_id="test_hotel",
        checkin=datetime.now(),
        checkout=datetime.now() + timedelta(days=2),
        residency="ru",
        language="ru",
        adults=2,
        children=[],
    )
    if hp.error:
        raise (Exception(hp.error))
    print(f"we have caught {len([h for h in hp.data.hotels[0].rates])} booking hashes")

    # Next, we are going to the booking form with a rate hash from the hotel page result
    order_id = "your_order_id"
    booking_form = make_booking_form(
        client=papi,
        order_id=order_id,
        rate_hash=hp.data.hotels[0].rates[0].book_hash,
        language="ru",
        ip_address="your_ip_address",
    )
    if booking_form.error:
        raise (Exception(booking_form.error))
    print("we have gotten the booking form!")

    # When we have the booking form data, we can go to the booking finish endpoint with payment type data
    result = make_booking_finish(
        client=papi,
        email="your_email_address",
        phone="your_phone_number",
        order_id=order_id,
        language="ru",
        guest_first_name="Test",
        guest_last_name="Test",
        pt_type=booking_form.data.payment_types[0].type,
        pt_amount=str(booking_form.data.payment_types[0].amount),
        pt_currency_code=booking_form.data.payment_types[0].currency_code,
    )
    if result.error:
        raise (Exception(result.error))
    if result.status == "ok":
        print("congratulates! the booking is done!")

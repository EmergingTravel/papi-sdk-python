from datetime import date, datetime, timedelta
from typing import List

from papi_sdk import APIv3
from papi_sdk.models.search.base_request import GuestsGroup
from papi_sdk.models.search.hotelpage.b2b import (
    B2BHotelPageRequest,
    B2BHotelPageResponse,
)


def get_hotel_page(
    client: APIv3,
    hotel_id: str,
    checkin: date,
    checkout: date,
    residency: str,
    language: str,
    adults: int,
    children: List[int],
) -> B2BHotelPageResponse:
    """
    The full documentation is available in https://docs.emergingtravel.com/?version=latest#67876b90-43ba-40e9-883b-a63a69b1be79
    """
    return client.b2b_search_hotel_page(
        data=B2BHotelPageRequest(
            id=hotel_id,
            checkin=checkin,
            checkout=checkout,
            residency=residency,
            language=language,
            guests=[GuestsGroup(adults=adults, children=children)],
        )
    )


if __name__ == "__main__":
    papi = APIv3(key="your_key")
    result = get_hotel_page(
        client=papi,
        hotel_id="test_hotel",
        checkin=datetime.now() + timedelta(days=20),
        checkout=datetime.now() + timedelta(days=21),
        residency="ru",
        language="ru",
        adults=2,
        children=[],
    )
    print(
        f"we have caught {len([h for h in result.data.hotels[0].rates])} booking hashes"
    )

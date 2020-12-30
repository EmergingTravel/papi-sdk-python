from datetime import date, datetime, timedelta
from typing import List

from papi_sdk import APIv3
from papi_sdk.models.search.base_request import GuestsGroup
from papi_sdk.models.search.region.b2b import B2BRegionRequest, B2BRegionResponse


def search_by_region(
    client: APIv3,
    region_id: int,
    checkin: date,
    checkout: date,
    residency: str,
    language: str,
    adults: int,
    children: List[int],
) -> B2BRegionResponse:
    """
    The full documentation is available in https://docs.emergingtravel.com/#5af3b9cf-34fa-4e5c-b290-d06a218851b6
    """
    return client.b2b_search_region(
        data=B2BRegionRequest(
            **{
                "region_id": region_id,
                "checkin": checkin,
                "checkout": checkout,
                "residency": residency,
                "language": language,
                "guests": [GuestsGroup(**{"adults": adults, "children": children})],
            }
        )
    )


if __name__ == "__main__":
    papi = APIv3(key="your_key")
    result = search_by_region(
        client=papi,
        region_id=0,
        checkin=datetime.now(),
        checkout=datetime.now() + timedelta(days=2),
        residency="ru",
        language="ru",
        adults=2,
        children=[],
    )
    print(f"we have caught {result.data.total_hotels} hotels")

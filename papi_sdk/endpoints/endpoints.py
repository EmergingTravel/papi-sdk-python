import os
from enum import Enum

BASE_PATH = os.environ.get("BASE_PATH", "https://api.worldota.net/")
BASE_PAY_PATH = os.environ.get("BASE_PAY_PATH", "https://api.payota.net/")


class Endpoint(str, Enum):
    OVERVIEW = BASE_PATH + "api/b2b/v3/overview/"
    HOTEL_INFO = BASE_PATH + "api/b2b/v3/hotel/info/"
    HOTEL_INFO_DUMP = BASE_PATH + "api/b2b/v3/hotel/info/dump/"
    ORDER_BOOKING_FORM = BASE_PATH + "api/b2b/v3/hotel/order/booking/form/"
    ORDER_BOOKING_FINISH = BASE_PATH + "api/b2b/v3/hotel/order/booking/finish/"
    ORDER_BOOKING_FINISH_STATUS = (
        BASE_PATH + "api/b2b/v3/hotel/order/booking/finish/status/"
    )
    ORDER_INFO = BASE_PATH + "api/b2b/v3/hotel/order/info/"
    SEARCH_HOTEL_PAGE = BASE_PATH + "api/b2b/v3/search/hp/"
    SEARCH_HOTELS = BASE_PATH + "api/b2b/v3/search/serp/hotels/"
    SEARCH_REGION = BASE_PATH + "api/b2b/v3/search/serp/region/"
    INIT_PARTNERS = BASE_PAY_PATH + "api/public/v1/manage/init_partners/"

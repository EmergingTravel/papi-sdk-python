from typing import Tuple

import requests
from requests.auth import HTTPBasicAuth

from papi_sdk.endpoints.endpoints import Endpoint
from papi_sdk.exceptions.base import InvalidAuthData
from papi_sdk.models.hotel_info import HotelInfoRequest, HotelInfoResponse
from papi_sdk.models.hotel_info_dump import HotelInfoDumpRequest, HotelInfoDumpResponse
from papi_sdk.models.init_partners import InitPartnerRequest, InitPartnerResponse
from papi_sdk.models.order_booking_finish.affiliate import (
    AffiliateHotelOrderBookingFinishRequest,
)
from papi_sdk.models.order_booking_finish.b2b import B2BHotelOrderBookingFinishRequest
from papi_sdk.models.order_booking_finish.base import HotelOrderBookingFinishResponse
from papi_sdk.models.order_booking_finish_status import (
    HotelOrderBookingFinishStatusRequest,
    HotelOrderBookingFinishStatusResponse,
)
from papi_sdk.models.order_booking_form import (
    AffiliateHotelOrderBookingFormResponse,
    B2BHotelOrderBookingFormResponse,
    OrderBookingFormRequest,
)
from papi_sdk.models.order_info.affiliate import (
    AffiliateHotelOrderInfoDataRequest,
    AffiliateHotelOrderInfoDataResponse,
)
from papi_sdk.models.order_info.b2b import (
    B2BHotelOrderInfoDataRequest,
    B2BHotelOrderInfoDataResponse,
)
from papi_sdk.models.overview import OverviewResponse
from papi_sdk.models.search.hotelpage.affiliate import (
    AffiliateHotelPageRequest,
    AffiliateHotelPageResponse,
)
from papi_sdk.models.search.hotelpage.b2b import (
    B2BHotelPageRequest,
    B2BHotelPageResponse,
)
from papi_sdk.models.search.hotels.affiliate import (
    AffiliateHotelsRequest,
    AffiliateHotelsResponse,
)
from papi_sdk.models.search.hotels.b2b import B2BHotelsRequest, B2BHotelsResponse
from papi_sdk.models.search.region.affiliate import (
    AffiliateRegionRequest,
    AffiliateRegionResponse,
)
from papi_sdk.models.search.region.b2b import B2BRegionRequest, B2BRegionResponse


class APIv3:
    def __init__(self, key: str):
        self.key_id, self.key = self._get_key_data(key)
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(self.key_id, self.key)

    @staticmethod
    def _get_key_data(key: str) -> Tuple[str, str]:
        try:
            key_id, key = key.split(":")
            return key_id, key
        except ValueError:
            raise InvalidAuthData(key)

    def _get_request(
        self, endpoint: str, params: dict = None, **requests_kwargs
    ) -> dict:
        """
        Inner method for GET requests.
        """
        response = self.session.get(endpoint, params=params, **requests_kwargs)
        return response.json()

    def _post_request(
        self, endpoint: str, json: dict = None, **requests_kwargs
    ) -> dict:
        """
        Inner method for POST requests.
        """
        response = self.session.post(endpoint, json=json, **requests_kwargs)
        return response.json()

    def overview(self, **requests_kwargs) -> OverviewResponse:
        """
        `Endpoints Overview
        <https://docs.emergingtravel.com/?version=latest#1ac1095b-caec-43ce-b8f2-aea779024883>`_.

        The list of all available for your contract endpoints and their settings.

        :param requests_kwargs: requests kwargs.
        """
        response = self._get_request(Endpoint.OVERVIEW.value, **requests_kwargs)
        return OverviewResponse(**response)

    def get_hotel_info(
        self, data: HotelInfoRequest, **requests_kwargs
    ) -> HotelInfoResponse:
        """
        `Hotel Data Search
        <https://docs.emergingtravel.com/?version=latest#cbbbb393-cb06-4bfe-a007-f5b07d1cf8a3>`_.

        Hotel data search by hotel identifier.
        It is supposed to be used only in case when available hotel is not included in
        the downloaded hotel data dump file - it can happen to new hotels in Emerging Travel Group inventory.
        This method can also be used for checking the content prior to reservation (with possible update).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.HOTEL_INFO.value, data=data.json(), **requests_kwargs
        )
        return HotelInfoResponse(**response)

    def get_hotel_info_dump(
        self, data: HotelInfoDumpRequest, **requests_kwargs
    ) -> HotelInfoDumpResponse:
        """
        `Hotel Data Dump
        <https://docs.emergingtravel.com/?version=latest#0b55c99a-7ef0-4a18-bbfe-fd1bdf35d08e>`_.

        Retrieving the data of all available Emerging Travel Group hotels as
        one archive for one language.
        Hotel's dump is generated every day,
        so the information retrieved from it shall be renewed with the recurrent download.

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.HOTEL_INFO_DUMP.value, data=data.json(), **requests_kwargs
        )
        return HotelInfoDumpResponse(**response)

    def b2b_order_booking_form(
        self, data: OrderBookingFormRequest, **requests_kwargs
    ) -> B2BHotelOrderBookingFormResponse:
        """
        `B2B Order Booking Form
        <https://docs.emergingtravel.com/?version=latest#18ad54c3-07dc-4515-9c02-4ff391ac6085>`_.

        Creating a new reservation.
        The process of reserving a rate includes several stages,
        their amount depends on whether there are 3d-secure check and
        fraud check (one or both of these checks can appear).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.ORDER_BOOKING_FORM.value, data=data.json(), **requests_kwargs
        )
        return B2BHotelOrderBookingFormResponse(**response)

    def affiliate_order_booking_form(
        self, data: OrderBookingFormRequest, **requests_kwargs
    ) -> AffiliateHotelOrderBookingFormResponse:
        """
        `Affiliate Order Booking Form
        <https://docs.emergingtravel.com/?version=latest#c27f9642-4111-4597-bca3-6c6e5bc6e34b>`_.

        Creating a new reservation.
        The process of reserving a rate includes several stages,
        their amount depends on whether there are 3d-secure check and
        fraud check (one or both of these checks can appear).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.ORDER_BOOKING_FORM.value, data=data.json(), **requests_kwargs
        )
        return AffiliateHotelOrderBookingFormResponse(**response)

    def b2b_order_booking_finish(
        self, data: B2BHotelOrderBookingFinishRequest, **requests_kwargs
    ) -> HotelOrderBookingFinishResponse:
        """
        `B2B Order Booking Finish
        <https://docs.emergingtravel.com/?version=latest#b79e9280-16da-4d51-b500-7f1c3bfd0f78>`_.

        The process of completing the reservation.

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.ORDER_BOOKING_FINISH.value, data=data.json(), **requests_kwargs
        )
        return HotelOrderBookingFinishResponse(**response)

    def affiliate_order_booking_finish(
        self, data: AffiliateHotelOrderBookingFinishRequest, **requests_kwargs
    ) -> HotelOrderBookingFinishResponse:
        """
        `Affiliate Order Booking Finish
        <https://docs.emergingtravel.com/?version=latest#571d227e-9970-445f-a0ed-a4a02ee1a468>`_.

        The process of completing the reservation.

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.ORDER_BOOKING_FINISH.value, data=data.json(), **requests_kwargs
        )
        return HotelOrderBookingFinishResponse(**response)

    def order_booking_finish_status(
        self, data: HotelOrderBookingFinishStatusRequest, **requests_kwargs
    ) -> HotelOrderBookingFinishStatusResponse:
        """
        `Order Booking Finish Status
        <https://docs.emergingtravel.com/?version=latest#09e1f183-0fef-49af-8c76-c8a8fa3d9036>`_.

        A status check for orders completion process made in the async (asynchronous) mode.
        Request is supposed to be used during reservation process only.

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.ORDER_BOOKING_FINISH_STATUS.value,
            data=data.json(),
            **requests_kwargs
        )
        return HotelOrderBookingFinishStatusResponse(**response)

    def b2b_order_info(
        self, data: B2BHotelOrderInfoDataRequest, **requests_kwargs
    ) -> B2BHotelOrderInfoDataResponse:
        """
        `B2B Order Information
        <https://docs.emergingtravel.com/?version=latest#ce9ab2ee-fec0-4850-9435-a894fd09ca0c>`_.

        Retrieving created order's information by the partner's booking identifier.
        Is relevant only for those reservations,
        that were initially successfully created (order/status request returned result.status key with "OK" value).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.ORDER_INFO.value, data=data.json(), **requests_kwargs
        )
        return B2BHotelOrderInfoDataResponse(**response)

    def affiliate_order_info(
        self, data: AffiliateHotelOrderInfoDataRequest, **requests_kwargs
    ) -> AffiliateHotelOrderInfoDataResponse:
        """
        `Affiliate Order Information
        <https://docs.emergingtravel.com/?version=latest#04563171-b039-4650-96a7-0e44c5550fc8>`_.

        Retrieving created order's information by the partner's booking identifier.
        Is relevant only for those reservations,
        that were initially successfully created (order/status request returned result.status key with "OK" value).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.ORDER_INFO.value, data=data.json(), **requests_kwargs
        )
        return AffiliateHotelOrderInfoDataResponse(**response)

    def b2b_search_hotel_page(
        self, data: B2BHotelPageRequest, **requests_kwargs
    ) -> B2BHotelPageResponse:
        """
        `B2B HotelPage
        <https://docs.emergingtravel.com/?version=latest#67876b90-43ba-40e9-883b-a63a69b1be79>`_.

        Hotel rates actualization.

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.SEARCH_HOTEL_PAGE.value, data=data.json(), **requests_kwargs
        )
        return B2BHotelPageResponse(**response)

    def affiliate_search_hotel_page(
        self, data: AffiliateHotelPageRequest, **requests_kwargs
    ) -> AffiliateHotelPageResponse:
        """
        `Affiliate HotelPage
        <https://docs.emergingtravel.com/?version=latest#3766a341-3b1c-4f66-84f5-a6f7600b9a79>`_.

        Hotel rates actualization.

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.SEARCH_HOTEL_PAGE.value, data=data.json(), **requests_kwargs
        )
        return AffiliateHotelPageResponse(**response)

    def b2b_search_hotels(
        self, data: B2BHotelsRequest, **requests_kwargs
    ) -> B2BHotelsResponse:
        """
        `B2B Hotels Search Engine Results Page
        <https://docs.emergingtravel.com/?version=latest#09dada83-ed9e-400e-a793-517d078e9df9>`_.

        Search Engine Results Page (SERP) - is the preliminary search of a hotel with
        available accommodation that meets the given search conditions.
        It is not recommended to let the users choose the rates from this
        method (full match with results of Hotelpage request is not expected).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.SEARCH_HOTELS.value, data=data.json(), **requests_kwargs
        )
        return B2BHotelsResponse(**response)

    def affiliate_search_hotels(
        self, data: AffiliateHotelsRequest, **requests_kwargs
    ) -> AffiliateHotelsResponse:
        """
        `Affiliate Hotels Search Engine Results Page
        <https://docs.emergingtravel.com/?version=latest#f1adf9d4-1666-4c9c-a319-138093eef31a>`_.

        Search Engine Results Page (SERP) - is the preliminary search of a hotel with
        available accommodation that meets the given search conditions.
        It is not recommended to let the users choose the rates from this
        method (full match with results of Hotelpage request is not expected).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.SEARCH_HOTELS.value, data=data.json(), **requests_kwargs
        )
        return AffiliateHotelsResponse(**response)

    def b2b_search_region(
        self, data: B2BRegionRequest, **requests_kwargs
    ) -> B2BRegionResponse:
        """
        `B2B Region Search Engine Results Page
        <https://docs.emergingtravel.com/?version=latest#5af3b9cf-34fa-4e5c-b290-d06a218851b6>`_.

        Search Engine Results Page (SERP) - is the preliminary search of a hotel with
        available accommodation that meets the given search conditions. I
        t is not recommended to let the users choose the rates from this
        method (full match with results of Hotelpage request is not expected).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.SEARCH_REGION.value, data=data.json(), **requests_kwargs
        )
        return B2BRegionResponse(**response)

    def affiliate_search_region(
        self, data: AffiliateRegionRequest, **requests_kwargs
    ) -> AffiliateRegionResponse:
        """
        `Affiliate Region Search Engine Results Page
        <https://docs.emergingtravel.com/?version=latest#c1d9a6a3-3d84-46ba-b490-84dbd24f95a9>`_.

        Search Engine Results Page (SERP) - is the preliminary search of a hotel with
        available accommodation that meets the given search conditions. I
        t is not recommended to let the users choose the rates from this
        method (full match with results of Hotelpage request is not expected).

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.SEARCH_REGION.value, data=data.json(), **requests_kwargs
        )
        return AffiliateRegionResponse(**response)

    def init_partners(
        self, data: InitPartnerRequest, **requests_kwargs
    ) -> InitPartnerResponse:
        """
        `Credit Card Data Tokenization
        <https://docs.emergingtravel.com/?version=latest#307703a9-e5d2-49ed-9466-22c4d697a03e>`_.

        Creating a payment token for the order with "is_need_credit_card_data": true payment type.
        Safe and secure credit card processing guaranteed by the PCI DSS standard.

        :param data: validated data.
        :param requests_kwargs: requests kwargs
        """
        response = self._post_request(
            Endpoint.INIT_PARTNERS.value, data=data.json(), **requests_kwargs
        )
        return InitPartnerResponse(**response)

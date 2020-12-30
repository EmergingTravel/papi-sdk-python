# pAPI SDK

pAPI SDK is a python SDK for [ETG APIv3](https://docs.emergingtravel.com/).
The abbreviation "pAPI" stands for "Partner API". 

## Requirements

- Python 3.6+
- requests
- pydantic

## Installation

```
pip install papi-sdk
```

## Quickstart

To start using ETG APIv3 you need a key, which you received after registration. 
A key is a combination of an `id` and `uuid`. These are passed into each request as a Basic Auth header after initialization.
`APIv3` supports all arguments provided by [requests](https://github.com/psf/requests), ex. `timeout`.

```python
from papi_sdk import APIv3


papi = APIv3(key='1000:022a2cf1-d279-02f3-9c3c-596aa09b827b', timeout=15)
```

Then you can use all available methods. Say you want to check an overview of the available methods (which is `api/b2b/v3/overview` endpoint), you do:

```python
overview = papi.overview(timeout=1)
```

Another example is downloading hotels dump with `api/b2b/v3/hotel/info/dump` endpoint:

```python
data = HotelInfoDumpRequest(language='ru')
dump = papi.get_hotel_info_dump(data=data)
print(dump.data.url)
```

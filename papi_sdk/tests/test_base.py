import unittest

from papi_sdk import APIv3


class BaseTest(unittest.TestCase):
    client = APIv3(key=f"1234:str(uuid.uuid4())")
    status_ok = "ok"
    status_error = "error"

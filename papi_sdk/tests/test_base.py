import unittest
import uuid
from unittest.mock import patch

from papi_sdk import APIv3


class BaseTest(unittest.TestCase):
    with patch("papi_sdk.api_v3.APIv3._get_version") as version:
        version.return_value = "0.0.1"
        client = APIv3(key=f"1234:{str(uuid.uuid4())}")
    status_ok = "ok"
    status_error = "error"

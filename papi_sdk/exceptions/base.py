class BaseError(Exception):
    pass


class InvalidAuthData(BaseError):
    def __init__(self, key: str):
        self.key = key

    def __str__(self):
        return f"Invalid key format {self.key}, must be key_id:key"

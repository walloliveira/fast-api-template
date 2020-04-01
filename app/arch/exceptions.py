from typing import Final


class HTTPException(Exception):
    status_code: Final[int]
    message: Final[str]

    def __init__(self, status_code: int, message: str):
        self.message = message
        self.status_code = status_code

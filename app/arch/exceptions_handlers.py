from typing import List, Final

from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from app.arch.exceptions import HTTPException


class Error(object):
    field: Final[str]
    message: Final[str]

    def __init__(self, field: str, message: str):
        self.message = message
        self.field = field

    def serialize(self) -> dict:
        return {
            'field': self.field,
            'message': self.message,
        }

    @classmethod
    def of(
            cls,
            field: str,
            message: str,
    ):
        return Error(field=field, message=message)


class ResponseError(object):
    status_code: Final[int]
    message: Final[str]
    errors: Final[List[Error]]

    def __init__(
            self,
            message: str,
            status_code: int,
            errors: List[Error] = [],
    ):
        self.message = message
        self.status_code = status_code
        self.errors = errors

    @classmethod
    def of_runtime_exception(cls, status_code: int, ex: Exception):
        return ResponseError(
            status_code=status_code,
            message=str(ex),
        )

    @classmethod
    def of_http_exception(cls, ex: HTTPException):
        return ResponseError(
            status_code=ex.status_code,
            message=ex.message,
        )

    @classmethod
    def of_request_validation_error(
            cls,
            status_code: int,
            request,
            exception: RequestValidationError,
    ):
        errors = cls._build_errors(exception)
        return ResponseError(
            errors=errors,
            status_code=status_code,
            message='',
        )

    @classmethod
    def _build_errors(cls, ex: RequestValidationError) -> list:
        errors = []
        for error in ex.errors():
            _, _, field = error.get('loc')
            message = error.get('msg')
            errors.append(Error.of(field, message))
        return errors

    def serialize(self) -> dict:
        return {
            'status_code': self.status_code,
            'message': self.message,
            'errors': [error.serialize() for error in self.errors],
        }

    def to_json(self) -> JSONResponse:
        return JSONResponse(
            content=self.serialize(),
            status_code=self.status_code,
        )


def handle_request_validation_error(
        request: Request,
        ex: RequestValidationError,
) -> JSONResponse:
    response_error = ResponseError.of_request_validation_error(
        HTTP_400_BAD_REQUEST,
        request,
        ex,
    )
    return response_error.to_json()


def handle_http_exception(
        request: Request,
        ex: HTTPException,
) -> JSONResponse:
    response_error = ResponseError.of_http_exception(ex)
    return response_error.to_json()


def handle_runtime_exception(
        request: Request,
        ex: Exception,
) -> JSONResponse:
    response_error = ResponseError.of_runtime_exception(
        HTTP_500_INTERNAL_SERVER_ERROR,
        ex,
    )
    return response_error.to_json()

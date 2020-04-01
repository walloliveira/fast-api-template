from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.arch.exceptions import HTTPException
from app.arch.exceptions_handlers import handle_runtime_exception, handle_http_exception, \
    handle_request_validation_error

api = FastAPI()

api.add_exception_handler(Exception, handle_runtime_exception)
api.add_exception_handler(HTTPException, handle_http_exception)
api.add_exception_handler(RequestValidationError, handle_request_validation_error)

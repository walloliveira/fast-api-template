from unittest import TestCase

from app import HTTPException


class TestHTTPException(TestCase):
    def test_given_that_the_http_exception_is_instantiate_then_status_code_must_equal_500_and_message_must_be_error(
            self):
        exception = HTTPException(
            status_code=500,
            message='error',
        )
        self.assertEqual(exception.status_code, 500)
        self.assertEqual(exception.message, 'error')

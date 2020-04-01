from unittest import TestCase
from unittest.mock import MagicMock, patch, call

from app import HTTPException
from app.arch.exceptions_handlers import Error, ResponseError, handle_request_validation_error, handle_http_exception, \
    handle_runtime_exception


class TestExceptionsHandlers(TestCase):
    request_mock = MagicMock()
    exception_mock = MagicMock()

    def setUp(self) -> None:
        self.request_mock.reset_mock()
        self.exception_mock.reset_mock()

    def test_given_that_the_error_is_instanced_when_the_method_serialize_is_called_then_return_must_be_a_dict(self):
        error = Error.of(field='field', message='Error')
        self.assertEqual(error.serialize(), {
            'field': 'field',
            'message': 'Error',
        })

    def test_given_that_the_response_error_is_instanced_by_the_method_of_http_exception_when_the_method_serialize_is_called_then_return_must_be_a_dict(
            self,
    ):
        exception = HTTPException(status_code=123, message='Message HTTP')
        response_error = ResponseError.of_http_exception(exception)
        self.assertEqual(response_error.serialize(), {
            'status_code': 123,
            'message': 'Message HTTP',
            'errors': [],
        })

    def test_given_that_the_response_error_is_instanced_by_the_method_of_runtime_exception_when_the_method_serialize_is_called_then_return_must_be_a_dict(
            self,
    ):
        exception = Exception('Error')
        response_error = ResponseError.of_runtime_exception(status_code=200, ex=exception)
        self.assertEqual(response_error.serialize(), {
            'status_code': 200,
            'message': 'Error',
            'errors': [],
        })

    @patch('app.arch.exceptions_handlers.JSONResponse')
    def test_given_that_the_response_error_is_instanced_by_the_method_of_http_exception_when_the_method_to_json_is_called_then_the_return_value_must_be_json_response(
            self,
            json_response_mock,
    ):
        exception = HTTPException(status_code=123, message='Message HTTP')
        json_response_mock.return_value = {}
        response_error = ResponseError.of_http_exception(exception)
        self.assertEqual(response_error.to_json(), {})
        self.assertEqual(len(json_response_mock.mock_calls), 1)
        json_response_mock.assert_has_calls([
            call(
                content={
                    'status_code': 123,
                    'message': 'Message HTTP',
                    'errors': [],
                },
                status_code=123,
            )
        ])

    @patch.object(Error, 'of')
    def test_given_that_the_response_error_is_instanced_by_the_method_of_request_validation_error_when_the_method_serialize_is_called_then_return_must_be_a_dict(
            self,
            of_mock,
    ):
        exception_mock = MagicMock()
        error_mock = MagicMock()
        error_mock.serialize.return_value = {}
        of_mock.side_effect = [error_mock]
        exception_mock.errors.return_value = [{
            'loc': ('', '', 'field'),
            'msg': 'Input Error',
        }]
        request = {}
        response_error = ResponseError.of_request_validation_error(
            status_code=400,
            request=request,
            exception=exception_mock,
        )
        self.assertEqual(response_error.serialize(), {
            'status_code': 400,
            'message': '',
            'errors': [{}],
        })
        of_mock.assert_called_once_with('field', 'Input Error')
        self.assertEqual(len(exception_mock.mock_calls), 1)
        exception_mock.assert_has_calls([
            call.errors(),
        ])
        self.assertEqual(len(error_mock.mock_calls), 1)
        error_mock.assert_has_calls([
            call.serialize(),
        ])

    @patch('app.arch.exceptions_handlers.ResponseError')
    def test_given_that_the_method_handle_request_validation_error_is_called_then_the_return_value_type_must_be_JSON_Response(
            self,
            response_error_mock,
    ):
        response_object_mock = MagicMock()
        response_error_mock.of_request_validation_error.side_effect = [response_object_mock]

        handle_request_validation_error(
            request=self.request_mock,
            ex=self.exception_mock,
        )

        self.assertEqual(len(response_error_mock.mock_calls), 1)
        response_error_mock.assert_has_calls([
            call.of_request_validation_error(
                400,
                self.request_mock,
                self.exception_mock,
            )
        ])
        self.assertEqual(len(response_object_mock.mock_calls), 1)
        response_object_mock.assert_has_calls([
            call.to_json(),
        ])
        self.exception_mock.assert_not_called()
        self.request_mock.assert_not_called()

    @patch('app.arch.exceptions_handlers.ResponseError')
    def test_given_that_the_method_handle_http_exception_is_called_then_the_return_value_type_must_be_JSON_Response(
            self,
            response_error_mock,
    ):
        response_object_mock = MagicMock()
        response_error_mock.of_http_exception.side_effect = [response_object_mock]

        handle_http_exception(
            request=self.request_mock,
            ex=self.exception_mock,
        )

        self.assertEqual(len(response_error_mock.mock_calls), 1)
        response_error_mock.assert_has_calls([
            call.of_http_exception(
                self.exception_mock,
            )
        ])
        self.assertEqual(len(response_object_mock.mock_calls), 1)
        response_object_mock.assert_has_calls([
            call.to_json(),
        ])
        self.exception_mock.assert_not_called()
        self.request_mock.assert_not_called()

    @patch('app.arch.exceptions_handlers.ResponseError')
    def test_given_that_the_method_handle_runtime_exception_is_called_then_the_return_value_type_must_be_JSON_Response(
            self,
            response_error_mock,
    ):
        response_object_mock = MagicMock()
        response_error_mock.of_runtime_exception.side_effect = [response_object_mock]

        handle_runtime_exception(
            request=self.request_mock,
            ex=self.exception_mock,
        )

        self.assertEqual(len(response_error_mock.mock_calls), 1)
        response_error_mock.assert_has_calls([
            call.of_runtime_exception(
                500,
                self.exception_mock,
            )
        ])
        self.assertEqual(len(response_object_mock.mock_calls), 1)
        response_object_mock.assert_has_calls([
            call.to_json(),
        ])
        self.exception_mock.assert_not_called()
        self.request_mock.assert_not_called()

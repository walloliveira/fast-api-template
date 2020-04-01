from typing import NoReturn
from unittest.mock import MagicMock, call

import pytest

from app.arch.use_case import UseCase, get_executor_use_case, ExecutorUseCase
from tests.unit.app.abstract_async_test import AbstractAsyncTest


class CreateColorUseCase(UseCase):

    def __init__(self):
        super().__init__([
            ('request', MagicMock),
        ])

    async def execute(self, request: MagicMock) -> NoReturn:
        request.to_domain()


class TestUseCase(AbstractAsyncTest):
    async def test_given_that_the_executor_use_case_is_instanced_when_method_execute_is_called_then_create_color_use_case_must_be_called(
            self):
        executor = get_executor_use_case()
        request_mock = MagicMock()
        await executor.execute(CreateColorUseCase, request=request_mock)
        methods_calls = request_mock.mock_calls
        self.assertEqual(len(methods_calls), 1)
        request_mock.assert_has_calls([
            call.to_domain(),
        ])

    async def test_given_that_the_executor_use_case_is_instanced_when_method_execute_is_called_then_an_error_must_be_thrown(
            self):
        executor = get_executor_use_case()
        with pytest.raises(Exception) as ex:
            await executor.execute(CreateColorUseCase, req='')
        self.assertEqual(str(ex.value), 'It is wrong')

    async def test_given_that_someone_tries_to_instantiate_an_use_case_then_an_error_must_be_thrown(self):
        use_case = UseCase([])
        with pytest.raises(NotImplementedError) as ex:
            await use_case.execute()
        self.assertEqual(str(ex.value), 'It is necessary')

    async def test_given_that_someone_tries_to_instantiate_an_executor_use_case_then_an_error_must_be_thrown(self):
        use_case = ExecutorUseCase([])
        with pytest.raises(NotImplementedError) as ex:
            await use_case.execute(int)
        self.assertEqual(str(ex.value), 'It is necessary')

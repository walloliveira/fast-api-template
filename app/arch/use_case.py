from abc import ABC
from typing import Type, NoReturn, Tuple, List


class UseCase(ABC):
    _requirements: List[Tuple[str, type]]

    def __init__(self, requirements: List[Tuple[str, type]]):
        self._requirements = requirements

    async def execute(self, **kwargs) -> NoReturn:
        raise NotImplementedError('It is necessary')


class ExecutorUseCase(UseCase):

    async def execute(self, use_case_clazz: Type[UseCase], **kwargs) -> NoReturn:
        raise NotImplementedError('It is necessary')


class ExecutorUseCaseImpl(ExecutorUseCase):

    def __init__(self):
        super().__init__([])

    async def execute(self, use_case_clazz: Type[UseCase], **kwargs) -> NoReturn:
        use_case = use_case_clazz()
        for requirement in use_case._requirements:
            name, clazz = requirement
            if not isinstance(kwargs.get(name), clazz):
                raise Exception('It is wrong')
        await use_case.execute(**kwargs)


def get_executor_use_case() -> ExecutorUseCase:
    return ExecutorUseCaseImpl()

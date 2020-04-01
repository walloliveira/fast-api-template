import asynctest
import pytest


class AbstractAsyncTest(asynctest.TestCase):
    pytestmark = pytest.mark.asyncio

import os

from dotenv import load_dotenv

_DOT_ENV_START_NAME = '.env.'
_DEFAULT_ENV = 'testing'

_ENV = os.getenv('API_ENV', _DEFAULT_ENV)
_dot_env_file = os.path.join(os.path.dirname(__file__), _DOT_ENV_START_NAME + _ENV.lower())
load_dotenv(dotenv_path=_dot_env_file, verbose=True)

DATABASE_URL = os.getenv('DATABASE_URL')
API_HOST = os.getenv('API_HOST')
API_PORT = int(os.getenv('API_PORT'))
API_LOG_LEVEL = os.getenv('API_LOG_LEVEL')
API_RELOAD = os.getenv('API_RELOAD')
API_TEST = eval(os.getenv('API_TEST'))
API_SECRET = os.getenv('API_SECRET')
WEB_CONCURRENCY = os.getenv('WEB_CONCURRENCY')
API_ENV = _ENV

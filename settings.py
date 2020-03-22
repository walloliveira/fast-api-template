import os

CONNECTION_URI = os.getenv('CONNECTION_URI')
API_HOST = os.getenv('API_HOST')
API_PORT = eval(os.getenv('API_PORT'))
API_LOG_LEVEL = os.getenv('API_LOG_LEVEL')
API_RELOAD = eval(os.getenv('API_RELOAD'))
API_TEST = eval(os.getenv('API_TEST'))
API_SECRET = os.getenv('API_SECRET')
WEB_CONCURRENCY = eval(os.getenv('WEB_CONCURRENCY'))

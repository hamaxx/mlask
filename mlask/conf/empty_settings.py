import os

SERVER = {
	'host': 'localhost',
	'port': 5000,
	'debug': True,
	'workers': 1,
}

ADMINS = []
LOG_FILE = 'mlask.log'
GUNICORN_LOG_FILE = 'mlask_gunicorn.log'

DATABASE = {
	'engine': 'sqlite', # mysql, sqlite
	'database': '',
	'user': '',
	'password': '',
	'host': '',
}
DATABASE_TEST = {
}

RUNNING_TESTS = False

MLASK_HOME_PATH = os.path.join(os.path.dirname(__file__), '../')

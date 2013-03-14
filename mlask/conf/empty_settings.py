import os

SERVER = {
	'host': 'localhost',
	'port': 5000,
	'debug': True,
	'workers': 1,
}

RUNNING_TESTS = False

MLASK_HOME_PATH = os.path.join(os.path.dirname(__file__), '../')

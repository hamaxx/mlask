import os

DEBUG = True
TESTING = False

SERVER = {
	'host': 'localhost',
	'port': 5000,
}

MODULES = []
TEST_MODULES = []
CONFIG_MODULES = []

MLASK_HOME_PATH = os.path.join(os.path.dirname(__file__), '../')


SERVICE_NAME = 'example'

MODULES = ['example.views',]
TEST_MODULES = ['example.tests',]

SERVER = {
	'host': 'localhost',
	'port': 5000,
	'debug': True,
	'workers': 1, # used only for rungunicorn
}

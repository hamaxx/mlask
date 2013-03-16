
SERVICE_NAME = '{{ empty_app }}'

MODULES = ['{{ empty_app }}.views',]
TEST_MODULES = ['{{ empty_app }}.tests',]

SERVER = {
	'host': 'localhost',
	'port': 5000,
	'debug': True,
	'workers': 1, # used only for rungunicorn
}

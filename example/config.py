
SERVICE_NAME = 'example'

DEBUG = True

SERVER = {
	'host': 'localhost',
	'port': 5000,
}

# Modules loaded when application is initialized.
MODULES = ['example.views',]

# Modules loaded when tests are run
TEST_MODULES = ['example.tests',]

# Modules with additional configuration. Loaded from first to last.
CONFIG_MODULES = []

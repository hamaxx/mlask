
SERVICE_NAME = '{{ empty_app }}'

DEBUG = True

SERVER = {
	'host': 'localhost',
	'port': 5000,
}

# Modules loaded when application is initialized.
MODULES = ['{{ empty_app }}.views',]

# Modules loaded when tests are run
TEST_MODULES = ['{{ empty_app }}.tests',]

# Modules with additional configuration. Loaded from first to last.
CONFIG_MODULES = []

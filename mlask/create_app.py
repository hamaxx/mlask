#!/usr/bin/env python

import os
import sys

def create_app():
	if len(sys.argv) < 2:
		print "Missing app name"
		return

	app_name = sys.argv[1]
	location = os.getcwd()

	files = {
		'__init__.py': '',
		'settings.py': """
SERVICE_NAME = '%s'

MODULES = ['%s.views',]
TEST_MODULES = ['%s.tests',]

SERVER = {
	'host': 'localhost',
	'port': 5000,
	'debug': True,
	'workers': 1,
}
""" % (app_name, app_name, app_name),
	'views.py': """
# Define you views here
""",
	'tests.py': """
# Define you tests here
""",
	'manage.py': """
#!/usr/bin/env python

import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
os.environ.setdefault("RLIBS_SETTINGS_MODULE", "%s.settings")

from mlask import manager

if __name__ == "__main__":
	manager.execute()
""" % app_name
	}

	app_dir = os.path.join(location, app_name)
	os.makedirs(app_dir)

	for fname, fcontent in files.iteritems():
		path = os.path.join(app_dir, fname)
		with open(path, 'w') as f:
			f.write(fcontent)

if __name__ == "__main__":
	create_app()

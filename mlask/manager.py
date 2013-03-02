import importlib

from flask import Flask

from mlask import conf
from mlask.commands import input_parser


def init_service():
	if hasattr(conf, 'SERVICE_MODULE'):
		mod = importlib.import_module(conf.SERVICE_MODULE)
		app = mod.app
	else:
		app = Flask(conf.SERVICE_NAME or __name__ )

	if hasattr(conf, 'MODULES'):
		with app.app_context():
			for module in conf.MODULES:
				importlib.import_module(module)

	return app


def execute():
	input_parser.load_commands()
	app = init_service()
	input_parser.run_command(app)

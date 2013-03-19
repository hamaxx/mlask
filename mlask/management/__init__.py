import os
import importlib

from flask import Flask

import mlask.conf
import mlask.management.input_parser


def _init_app():
	# app.config is not yet available
	if "MLASK_CONFIG_MODULE" in os.environ:
		config = importlib.import_module(os.environ["MLASK_CONFIG_MODULE"])
	else:
		config = None

	if config and hasattr(config, 'FLASK_APP'):
		app = importlib.import_module(config.FLASK_APP)
	else:
		service_name = 'mlask'
		if config and hasattr(config, 'SERVICE_NAME'):
			service_name = config.SERVICE_NAME

		app = Flask(service_name)

	return app


def _import_modules(app):
	if hasattr(app.config, 'MODULES'):
		with app.app_context():
			for module in app.config.MODULES:
				importlib.import_module(module)


def execute():
	app = _init_app()
	mlask.conf.init(app)

	mlask.management.input_parser.load_commands(app)

	_import_modules(app)
	mlask.management.input_parser.run_command(app)

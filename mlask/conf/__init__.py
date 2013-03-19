import os

from flask import Config


def _flask_config_getattr(self, attr):
	"""Expose flask config keys as attributes"""

	try:
		return self[attr]
	except KeyError:
		raise AttributeError("AttributeError: '%s' object has no attribute '%s'" % (self.__class__.__name__, attr))


def init(app):
	"""Initialize mlask and flask config."""

	Config.__getattr__ = _flask_config_getattr

	app.config.from_object('mlask.conf.empty_config')

	if "MLASK_CONFIG_MODULE" in os.environ:
		app.config.from_object(os.environ["MLASK_CONFIG_MODULE"])

	for conf_module in app.config.CONFIG_MODULES:
		app.config.from_object(os.environ["MLASK_CONFIG_MODULE"])

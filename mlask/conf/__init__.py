import os
import importlib

_initialized = False
_settings_module = None

def parse(setts):
	# django does the same thing
	for setting in dir(setts):
		if setting == setting.upper():
			setting_value = getattr(setts, setting)
			globals()[setting] = setting_value

def init():
	global _initialized, _settings_module

	from mlask.conf import empty_settings
	parse(empty_settings)

	if "RLIBS_SETTINGS_MODULE" in os.environ:
		setts = importlib.import_module(os.environ["RLIBS_SETTINGS_MODULE"])
		_settings_module = setts
		parse(setts)

	_initialized = True

def clear():
	for setting in globals():
		if setting == setting.upper():
			globals()[setting] = None

if not _initialized:
	init()

import sys
import argparse

from mlask.management.commands import BaseCommand

import mlask.management.commands.basic_commands
import mlask.management.commands.test
import mlask.management.commands.startapp


_commands = {}
_parser = None

def load_commands():
	global _parser

	_parser = argparse.ArgumentParser(description='Manage flask app.')
	subparsers = _parser.add_subparsers(dest='action_name')

	command_classes = BaseCommand.__subclasses__()
	for CommandClass in command_classes:
		c = CommandClass(subparsers)
		c.load()
		_commands[c.__command_name__] = c

def run_command(app):
	inp = _parser.parse_args(sys.argv[1:])
	with app.app_context():
		_commands[inp.action_name].run(inp)

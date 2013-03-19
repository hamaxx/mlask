import os
import sys
import unittest
import importlib
import inspect

from mlask.management.commands import BaseCommand

from flask import current_app as app

class Test(BaseCommand):
	__help__ = 'Runs all test in "TEST_MODULES"'

	_coverage = None

	def update_parser(self, parser):
		parser.add_argument('testname', nargs='?', help="Run specific test")
		parser.add_argument('--coverage', action='store_true', default=False, help="calculate test code coverage")
		parser.add_argument('--htmlreport', action='store_true', default=False, help="export code coverage report as html")

	def find_project_files(self):
		# TODO: Use app.config.TEST_MODULES to determine project files

		return None

		"""
		pyfiles = []
		basedir = os.path.dirname(app.config._settings_module.__file__)
		for r,d,f in os.walk(basedir):
			for files in f:
				if files.endswith(".py"):
					pyfiles.append(os.path.abspath(os.path.join(r,files)))

		return pyfiles
		"""

	def coverage_start(self, options):
		if options.coverage:
			try:
				import coverage
			except ImportError:
				raise ImportError('To use --coverage install coverage.py package')

			self._coverage = coverage.coverage()
			self._coverage.start()

	def coverage_report(self, options):
		if not self._coverage:
			return
		self._coverage.stop()
		project_files = self.find_project_files()
		print self._coverage.report(include=project_files)
		if options.htmlreport:
			self._coverage.html_report(directory="coverage_report", include=project_files)

	def load(self):
		app.config.TESTING = True

	def _find_subclasses(self, module, clazz):
		return [ cls for name, cls in inspect.getmembers(module) if inspect.isclass(cls) and issubclass(cls, clazz) ]

	def _get_matching_submodule_path(self, m1_str, m2_str):
		if not m1_str or not m2_str:
			return None

		m1 = m1_str.split('.')
		m2 = m2_str.split('.')[:len(m1)]

		for i, m2_p in enumerate(m2):
			if m1[i] != m2_p:
				raise AttributeError()

		return '.'.join(m1[len(m2):])

	def _load_test_suits(self, options):
		test_loader = unittest.defaultTestLoader

		test_suites = []
		if hasattr(app.config, 'TEST_MODULES'):
			for module in app.config.TEST_MODULES:
				tmod = importlib.import_module(module)

				try:
					test_path = self._get_matching_submodule_path(options.testname, module)
					if test_path:
						test_suite = test_loader.loadTestsFromName(test_path, module=tmod)
					else:
						test_suite = test_loader.loadTestsFromModule(tmod)
					test_suites.append(test_suite)
				except AttributeError:
					pass

		return unittest.TestSuite(test_suites)

	def run(self, options):
		test_runner = unittest.TextTestRunner(verbosity=1)

		self.coverage_start(options)
		result = test_runner.run(self._load_test_suits(options))
		self.coverage_report(options)

		exit_status = 0 if result.wasSuccessful() else 1
		sys.exit(exit_status)


import sys
import code

from mlask.management.commands import BaseCommand
from mlask import conf

from flask import current_app as app

class RunServer(BaseCommand):
	__help__ = 'Starts testing server'

	def update_parser(self, parser):
		parser.add_argument('--host', type=str, default=conf.SERVER['host'])
		parser.add_argument('--port', type=int, default=conf.SERVER['port'])
		parser.add_argument('--debug', action='store_true', default=conf.SERVER['debug'])

	def run(self, options):
		app.run(options.host, options.port, debug=options.debug)


class RunGunicorn(BaseCommand):
	__help__ = 'Starts Gunicorn server'

	def update_parser(self, parser):
		parser.add_argument('--logfile', type=str, default=getattr(conf, 'GUNICORN_LOG_FILE', 'gunicorn.log'))
		parser.add_argument('--host', type=str, default=conf.SERVER['host'])
		parser.add_argument('--port', type=int, default=conf.SERVER['port'])
		parser.add_argument('--workers', type=int, default=(conf.SERVER['workers'] if 'workers' in conf.SERVER else 1))

	def run(self, options):
		try:
			from gunicorn.app.base import Application
		except ImportError:
			raise ImportError('To use rungunicorn install gunicorn package')

		class WSGIServer(Application):
			def init(self, parser, opts, args):
				return {
					'bind': '%s:%s' % (options.host, options.port),
					'workers': options.workers,
					'errorlog': options.logfile,
				}
			def load(self):
				return app

		sys.argv = [sys.argv[0]]
		WSGIServer().run()


class Shell(BaseCommand):
	__help__ = 'Starts interactive shell with defined "app" and "conf" vars'

	def run(self, options):
		vars = {'conf': conf, 'app': app}

		try:
			import readline
		except ImportError:
			print "Please install readline to enable command line editing."
		else:
			import rlcompleter
			readline.set_completer(rlcompleter.Completer(vars).complete)
			if 'libedit' in readline.__doc__:
				readline.parse_and_bind("bind ^I rl_complete")
			else:
				readline.parse_and_bind("tab:complete")

		code.interact(local=vars)


class SyncDB(BaseCommand):
	__help__ = 'Creates all tables defined by SQLAlchemy declarative'

	def run(self, options):
		from flask.ext.sqlalchemy import SQLAlchemy

		db = SQLAlchemy(app)
		db.create_all()

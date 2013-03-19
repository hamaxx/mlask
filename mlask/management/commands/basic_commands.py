import sys
import code

from mlask.management.commands import BaseCommand

from flask import current_app as app

class RunServer(BaseCommand):
	__help__ = 'Starts testing server'

	def update_parser(self, parser):
		parser.add_argument('--host', type=str, default=app.config.SERVER['host'])
		parser.add_argument('--port', type=int, default=app.config.SERVER['port'])
		parser.add_argument('--debug', action='store_true', default=app.config.DEBUG)

	def run(self, options):
		app.run(options.host, options.port, debug=options.debug)


class RunGunicorn(BaseCommand):
	__help__ = 'Starts Gunicorn server'

	def update_parser(self, parser):
		parser.add_argument('--logfile', type=str, default=getattr(app.config, 'GUNICORN_LOG_FILE', 'gunicorn.log'))
		parser.add_argument('--host', type=str, default=app.config.SERVER['host'])
		parser.add_argument('--port', type=int, default=app.config.SERVER['port'])
		parser.add_argument('--workers', type=int, default=(app.config.SERVER['workers'] if 'workers' in app.config.SERVER else 1))

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
	__help__ = 'Starts interactive shell with defined app'

	def run(self, options):
		vars = {'app': app}

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

from flask.ext.sqlalchemy import SQLAlchemy
from flask import current_app as app

from mlask import conf


if conf.RUNNING_TESTS:
	conf.DATABASE = dict(conf.DATABASE.items() + conf.DATABASE_TEST.items())

def get_database_uri(db_conf):
	uri = ''
	if db_conf['engine'] == 'mysql':
		uri = 'mysql://%(user)s:%(password)s@%(host)s/%(database)s' % db_conf
	elif db_conf['engine'] == 'sqlite':
		uri = 'sqlite:///%(database)s' % db_conf
	return uri

for db_name, db_conf in conf.DATABASE.iteritems():
	if db_name == 'default':
		app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri(db_conf)
	else:
		if not 'SQLALCHEMY_BINDS' in app.config:
			app.config['SQLALCHEMY_BINDS'] = {}
		app.config['SQLALCHEMY_BINDS'][db_name] = get_database_uri(db_conf)

db = SQLAlchemy(app)

def init_db():
	db.create_all()


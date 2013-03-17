"""
mlask is still fun
==================

Mlask brings a bit of django like structure to
`Flask <http://flask.pocoo.org/>`_ apps.

Installation:
-------------

::

    pip install mlask

Create your first app:
----------------------

To create the skeleton run:

::

    mlask-admin.py startapp your_apps_name

This command will create a folder named your_apps_name with the
following files:

* manage.py
* settings.py
* tests.py
* views.py

For the "hello world" examples check "views.py" and "tests.py".

When you're ok with your first app, start the testing server by running:

::

    python manage.py runserver

Then run the tests I'm sure you've written:

::

    python manage.py test

Edit "settings.py" to change server settings, add aditional modules to
your app and to define your own settings. All uppercase variables from
"settings.py" are accessible from "mlask.conf" module.

And that's mostly it. For full Flask documentation visit
`flask.pocoo.org/docs/api/ <http://flask.pocoo.org/docs/api/>`_.

All built in commands:
----------------------

::

    runserver       Starts testing server
    rungunicorn     Starts Gunicorn server
    shell           Starts interactive shell with defined "app" and "conf" vars
    syncdb          Creates all tables defined by SQLAlchemy declarative
    test            Runs all tests in "settings.TEST_MODULES"
    startapp        Creates an app direcory structure for the given app name in the current directory

Define your own command:
------------------------

Create a file mycommands.py with the following content:

::

    from mlask.management.commands import BaseCommand

    class ExampleCommand(BaseCommand):
        __command_name__ = 'example' #optional
        __help__ = 'Short help' #optional

        def update_parser(self, parser):
            # Define rules for parsing the input.
            # Check argparse for full documentation.

            parser.add_argument('text', help="Text to print")

        def run(self, options):
            print options.text

Add "your_apps_name.mycommands" module to settings.py "MODULES" and
test it out by running:

::

    python manage.py example "Hello"
"""


from setuptools import setup

setup(name='Mlask',
		version='0.1',
		description='manage.py for Flask',
		author='Jure Ham',
		author_email='jure.ham@zemanta.com',
		long_description=__doc__,
		url='https://github.com/hamaxx/mlask',
		license="BSD",
		packages=['mlask', 'mlask.bin', 'mlask.conf', 'mlask.management', 'mlask.management.commands'],
		scripts=['mlask/bin/mlask-admin.py'],
		install_requires=[
			'Flask',
		],
		classifiers=[
			'Development Status :: 4 - Beta',
		],
	)

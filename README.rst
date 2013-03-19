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
* config.py
* tests.py
* views.py

For the "hello world" examples check "views.py" and "tests.py".

When you're ok with your first app, start the testing server by running:

::

    python manage.py runserver

Then run the tests I'm sure you've written:

::

    python manage.py test

Edit "config.py" to change server settings, add aditional modules to
your app and to define your own configuration. All uppercase variables from
"config.py" are accessible from "app.config" module.
More on Flask configuration: `flask.pocoo.org/docs/config/ <http://flask.pocoo.org/docs/config/>`_.

And that's mostly it. For full Flask documentation visit
`flask.pocoo.org/docs/api/ <http://flask.pocoo.org/docs/api/>`_.

All built in commands:
----------------------

::

    runserver       Starts testing server
    rungunicorn     Starts Gunicorn server
    shell           Starts interactive shell with defined app
    syncdb          Creates all tables defined by SQLAlchemy declarative
    test            Runs all tests in "config.TEST_MODULES"
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

Add "your_apps_name.mycommands" module to config.py "MODULES" and
test it out by running:

::

    python manage.py example "Hello"


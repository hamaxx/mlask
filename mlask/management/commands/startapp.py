import os

from mlask.management.commands import BaseCommand
from mlask import conf

class StartApp(BaseCommand):
	__command_name__ = 'startapp'
	__help__ = 'Creates an app direcory structure for the given app name in the current directory.'

	def update_parser(self, parser):
		parser.add_argument('appname', help="Name of the app")

	def run(self, options):
		app_name = options.appname

		location = os.getcwd()
		app_dir = os.path.join(location, app_name)
		os.makedirs(app_dir)

		template_dir = os.path.join(conf.MLASK_HOME_PATH, 'conf/empty_app/')

		app_name_tag = '{{ empty_app }}'

		for fn in os.listdir(template_dir):
			src_path  = os.path.join(template_dir, fn)
			dest_path = os.path.join(app_dir, fn)

			with open(src_path, 'r') as src_file:
				template = src_file.read()
				template = template.replace(app_name_tag, app_name)

				with open(dest_path, 'w') as dest_file:
					dest_file.write(template)


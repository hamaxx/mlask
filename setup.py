from setuptools import setup, find_packages

setup(name='Mlask',
		version='0.1',
		description='Mlask - manage.py for Flask',
		author='Jure Ham',
		author_email = 'jure.ham@zemanta.com',
		license = "BSD",
		packages=['mlask'] + [ 'mlask.%s' % package for package in find_packages('mlask') ],
		scripts = ['mlask/bin/mlask-admin.py'],

		install_requires=[
			'Flask',
		],
	)

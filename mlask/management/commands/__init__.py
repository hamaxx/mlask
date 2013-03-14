
class BaseCommand(object):

	__command_name__ = None
	__help__ = None

	_parser = None

	def __init__(self, subparsers):
		self._parser = None
		self.__command_name__ = self.__command_name__ or self.__class__.__name__.lower()
		self.__help__ = self.__help__ or  'Runs %s' % self.__class__.__name__

		self._init_parser(subparsers)

	def update_parser(self, parser):
		pass

	def run(self, options):
		pass

	def load(self):
		pass

	def _help(self):
		if hasattr(self, '__help__'):
			return self.__help__

	def _init_parser(self, subparsers):
		self._parser = subparsers.add_parser(self.__command_name__, help=self.__help__)
		self.update_parser(self._parser)

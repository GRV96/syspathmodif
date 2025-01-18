import sys


def sm_contains(module_name):
	"""
	Indicates whether dictionary sys.modules contains the module or package
	whose name is the argument.

	Args:
		module_name (str): the name of a module or package.

	Returns:
		bool: True if sys.modules contains argument module_name, False
			otherwise.
	"""
	return module_name in sys.modules


__all__ = [sm_contains.__name__]

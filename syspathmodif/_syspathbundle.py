from strath import ensure_path_is_str

from ._no_path_check import\
	sp_append_no_path_check,\
	sp_remove_no_path_check


class SysPathBundle:
	"""
	Upon instantiation, a bundle stores several paths and adds them to list
	sys.path. When a bundle is cleared, it removes all its paths from sys.path
	and erases its content. Thus, this class facilitates the simultaneous
	addition and removal of many paths.

	The destructor __del__ clears the bundle.
	"""

	def __init__(self, content):
		"""
		The constructor needs the paths (type str or pathlib.Path) to store in
		this instance and add to sys.path. If a path in argument content is
		None or is already in sys.path, this instance will not store it.

		Args:
			content (generator, list, set or tuple): the paths to store in this
				instance.

		Raises:
			TypeError: if a path is not None and not of type str or
				pathlib.Path.
		"""
		self._content = list()
		self._fill_content(content)

	def __del__(self):
		"""
		Clears the bundle by calling method clear.
		"""
		self.clear()

	def clear(self):
		"""
		Removes the paths stored in this instance from sys.path and erases
		this instance's content.
		"""
		while True:
			try:
				path = self._content.pop() # Can raise IndexError.
				sp_remove_no_path_check(path)
			except IndexError:
				# All paths have been removed.
				break

	def _fill_content(self, content):
		for path in content:
			path = ensure_path_is_str(path, True)

			if sp_append_no_path_check(path):
				# Any path in self._content is a string.
				self._content.append(path)

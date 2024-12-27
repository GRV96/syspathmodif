from strath import ensure_path_is_str

from ._no_path_check import\
	sp_append_no_path_check,\
	sp_remove_no_path_check


class SysPathBundle:

	def __init__(self, content):
		self._content = list()
		self._fill_content(content)

	def __del__(self):
		self.clear()

	def clear(self):
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

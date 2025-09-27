from inspect import stack
from pathlib import Path
from typing import Iterable

from .individual_paths_no_type_check import sp_prepend_no_type_check
from .syspathbundle import SysPathBundle


def _get_calling_file() -> Path:
	return Path(stack()[2].filename)


def sp_prepend_parent(parent_index: int) -> Path | None:
	"""
	Given the index of a parent directory of the file that calls this function,
	the function prepends the parent path to sys.path. The prepending succeeds
	if sys.path does not already contain the parent path. Otherwise, sys.path
	is not changed.

	Let be a pathlib.Path instance p representing the path to the calling file.
	The parent directory identified by an index i passed to this function
	matches the path returned by p.parents[i].

	Args:
		parent_index: the index of the parent path.

	Returns:
		Path: the path to the parent directory if the prepending succeeds, None
			if it fails.

	Raises:
		IndexError: if argument parent_index is out of bounds.
	"""
	calling_file = _get_calling_file()
	parent_dir = calling_file.parents[parent_index]
	success = sp_prepend_no_type_check(str(parent_dir))
	return parent_dir if success else None


def sp_prepend_parent_bundle(
		parent_indices: Iterable[int],
		cleared_on_del: bool = False
	) -> SysPathBundle:
	calling_file = _get_calling_file()
	gen_parent_dirs = (calling_file.parents[i] for i in parent_indices)
	return SysPathBundle(gen_parent_dirs, cleared_on_del)


__all__ = [
	sp_prepend_parent.__name__,
	sp_prepend_parent_bundle.__name__
]

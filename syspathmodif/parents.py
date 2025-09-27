from inspect import stack
from pathlib import Path
from typing import Iterable

from .individual_paths_no_type_check import sp_prepend_no_type_check
from .syspathbundle import SysPathBundle


def _get_calling_file() -> Path:
	return Path(stack()[2].filename)


def sp_prepend_parent(parent_index: int) -> Path | None:
	calling_file = _get_calling_file()
	parent_dir = calling_file.parents[parent_index]
	success = sp_prepend_no_type_check(str(parent_dir))
	return parent_dir if success else None


def sp_prepend_parents_bundle(
		parent_indices: Iterable[int],
		cleared_on_del: bool = False
	) -> SysPathBundle:
	calling_file = _get_calling_file()
	gen_parent_dirs = (calling_file.parents[i] for i in parent_indices)
	return SysPathBundle(gen_parent_dirs, cleared_on_del)


__all__ = [
	sp_prepend_parent.__name__,
	sp_prepend_parents_bundle.__name__
]

import pytest

from pathlib import Path
import sys

from _test_utils import\
	REPO_ROOT,\
	assert_path_is_present,\
	index_in_sys_path,\
	reset_sys_path

sys.path.insert(0, str(REPO_ROOT))
from syspathmodif import\
	sp_prepend_parent_bundle
reset_sys_path()


_THIS_FILE = Path(__file__).resolve()


def test_parent_bundle():
	try:
		bundle = sp_prepend_parent_bundle((0, 1, 2))

		parent0 = _THIS_FILE.parents[0]
		assert_path_is_present(parent0, bundle, True, False)
		assert index_in_sys_path(parent0) == 2

		parent1 = _THIS_FILE.parents[1]
		assert_path_is_present(parent1, bundle, True, True)
		assert index_in_sys_path(parent1) == 1

		parent2 = _THIS_FILE.parents[2]
		assert_path_is_present(parent2, bundle, True, True)
		assert index_in_sys_path(parent2) == 0

	finally:
		reset_sys_path()


def test_index_out_of_bounds():
	try:
		with pytest.raises(IndexError):
			sp_prepend_parent_bundle((0, 1, 2, 2025))
	finally:
		reset_sys_path()


def test_prepend_parent_minus1():
	try:
		parent_minus1 = _THIS_FILE.parents[-1]
		bundle = sp_prepend_parent_bundle((-1,))
		assert_path_is_present(parent_minus1, bundle, True, True)
		assert index_in_sys_path(parent_minus1) == 0
	finally:
		reset_sys_path()

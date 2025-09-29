import pytest

from pathlib import Path
import sys

from _test_utils import\
	INIT_SYS_PATH,\
	REPO_ROOT,\
	index_in_sys_path,\
	reset_sys_path

sys.path.insert(0, str(REPO_ROOT))
from syspathmodif import\
	sp_prepend_parent
reset_sys_path()


_THIS_FILE = Path(__file__).resolve()


def test_prepend_parent0():
	try:
		parent0 = sp_prepend_parent(0)
		assert sys.path == INIT_SYS_PATH
		assert parent0 is None
	finally:
		reset_sys_path()


def test_prepend_parent1():
	try:
		parent1 = sp_prepend_parent(1)
		assert parent1 == _THIS_FILE.parents[1]
		assert index_in_sys_path(parent1) == 0
	finally:
		reset_sys_path()


def test_prepend_parent2():
	try:
		parent2 = sp_prepend_parent(2)
		assert parent2 == _THIS_FILE.parents[2]
		assert index_in_sys_path(parent2) == 0
	finally:
		reset_sys_path()


def test_index_out_of_bounds():
	try:
		with pytest.raises(IndexError):
			sp_prepend_parent(2025)
	finally:
		reset_sys_path()


def test_prepend_parent_minus1():
	try:
		parent_minus1 = sp_prepend_parent(-1)
		assert parent_minus1 == _THIS_FILE.parents[-1]
		assert index_in_sys_path(parent_minus1) == 0
	finally:
		reset_sys_path()

import pytest

from pathlib import Path
import sys


_INIT_SYS_PATH = list(sys.path)

_LOCAL_DIR = Path(__file__).parent.resolve()
_PARENT_DIR = _LOCAL_DIR.parent


sys.path.append(str(_PARENT_DIR))
from syspathmodif import\
	sp_append,\
	sp_contains,\
	sp_remove
sys.path = _INIT_SYS_PATH


def test_sp_contains_str():
	# This test does not change the content of sys.path.
	assert sp_contains(str(_LOCAL_DIR))
	assert not sp_contains(str(_PARENT_DIR))


def test_sp_contains_pathlib():
	# This test does not change the content of sys.path.
	assert sp_contains(_LOCAL_DIR)
	assert not sp_contains(_PARENT_DIR)


def test_sp_contains_exception():
	# This test does not change the content of sys.path.
	except_msg = "A path must be of type str or pathlib.Path."
	with pytest.raises(TypeError, match = except_msg):
		sp_contains(3.14159)


def test_sp_append_and_remove_str():
	try:
		sp_append(str(_PARENT_DIR))
		assert sp_contains(str(_PARENT_DIR))
		sp_remove(str(_PARENT_DIR))
		assert not sp_contains(str(_PARENT_DIR))
	finally:
		sys.path = _INIT_SYS_PATH


def test_sp_append_and_remove_pathlib():
	try:
		sp_append(_PARENT_DIR)
		assert sp_contains(_PARENT_DIR)
		sp_remove(_PARENT_DIR)
		assert not sp_contains(_PARENT_DIR)
	finally:
		sys.path = _INIT_SYS_PATH

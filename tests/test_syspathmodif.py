import pytest

from pathlib import Path
import sys


_INIT_SYS_PATH = list(sys.path)

_LOCAL_DIR = Path(__file__).parent.resolve()
_REPO_ROOT = _LOCAL_DIR.parent
_LIB_DIR = _REPO_ROOT/"syspathmodif"


sys.path.append(str(_REPO_ROOT))
from syspathmodif import\
	sp_append,\
	sp_contains,\
	sp_remove
sys.path = list(_INIT_SYS_PATH)


def reset_sys_path():
	sys.path = list(_INIT_SYS_PATH)


def test_sp_contains_str():
	# This test does not change the content of sys.path.
	dir0 = str(sys.path[0])
	assert sp_contains(dir0)
	assert not sp_contains(str(_LIB_DIR))


def test_sp_contains_pathlib():
	# This test does not change the content of sys.path.
	dir0 = Path(sys.path[0])
	assert sp_contains(dir0)
	assert not sp_contains(_LIB_DIR)


def test_sp_contains_exception():
	# This test does not change the content of sys.path.
	except_msg = "A path must be of type str or pathlib.Path."
	with pytest.raises(TypeError, match = except_msg):
		sp_contains(3.14159)


def test_sp_append_and_remove_str():
	try:
		sp_append(str(_LIB_DIR))
		assert sp_contains(str(_LIB_DIR))
		sp_remove(str(_LIB_DIR))
		assert not sp_contains(str(_LIB_DIR))
	finally:
		reset_sys_path()


def test_sp_append_and_remove_pathlib():
	try:
		sp_append(_LIB_DIR)
		assert sp_contains(_LIB_DIR)
		sp_remove(_LIB_DIR)
		assert not sp_contains(_LIB_DIR)
	finally:
		reset_sys_path()

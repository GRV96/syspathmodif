import pytest

from pathlib import Path
import sys

from strath import ensure_path_is_str


_INIT_SYS_PATH = list(sys.path)

_LOCAL_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _LOCAL_DIR.parent
_LIB_DIR = _REPO_ROOT/"syspathmodif"


def _reset_sys_path():
	# Copying the list is necessary to preserve the initial state.
	sys.path = list(_INIT_SYS_PATH)


sys.path.append(str(_REPO_ROOT))
from syspathmodif import SysPathBundle
_reset_sys_path()


def assert_path_is_present(some_path, bundle, is_in_sys_path, is_in_bundle):
	some_path = ensure_path_is_str(some_path, True)

	assert (some_path in sys.path) == is_in_sys_path

	if bundle is not None:
		assert (some_path in bundle._content) == is_in_bundle


def test_init():
	try:
		bundle = SysPathBundle((_LOCAL_DIR, _REPO_ROOT, _LIB_DIR))

		assert_path_is_present(_LOCAL_DIR, bundle, True, False)
		assert_path_is_present(_REPO_ROOT, bundle, True, True)
		assert_path_is_present(_LIB_DIR, bundle, True, True)

	finally:
		_reset_sys_path()


def test_clear():
	try:
		bundle = SysPathBundle((_LOCAL_DIR, _REPO_ROOT, _LIB_DIR))
		bundle.clear()

		assert_path_is_present(_LOCAL_DIR, bundle, True, False)
		assert_path_is_present(_REPO_ROOT, bundle, False, False)
		assert_path_is_present(_LIB_DIR, bundle, False, False)

		assert sys.path == _INIT_SYS_PATH

	finally:
		_reset_sys_path()


def test_del():
	try:
		bundle = SysPathBundle((_LOCAL_DIR, _REPO_ROOT, _LIB_DIR))
		del bundle

		assert_path_is_present(_LOCAL_DIR, None, True, False)
		assert_path_is_present(_REPO_ROOT, None, False, False)
		assert_path_is_present(_LIB_DIR, None, False, False)

		assert sys.path == _INIT_SYS_PATH

	finally:
		_reset_sys_path()

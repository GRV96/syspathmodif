# __all__ declared at the module's end

from pathlib import Path
import sys

# strath is a dependency of syspathmodif.
from strath import ensure_path_is_str


INIT_SYS_PATH = list(sys.path)
"""
The initial content of sys.path.
"""

TEST_DIR = Path(__file__).resolve().parent
"""
The tests' directory.
"""

REPO_ROOT = TEST_DIR.parent
"""
This repository's root directory.
"""

LIB_DIR = REPO_ROOT/"syspathmodif"
"""
The library's directory.
"""


def reset_sys_path() -> None:
	"""
	Assigns a copy of INIT_SYS_PATH to sys.path.
	"""
	# Copying the list is necessary to preserve the initial state.
	sys.path = list(INIT_SYS_PATH)


sys.path.insert(0, str(REPO_ROOT))
from syspathmodif import SysPathBundle
reset_sys_path()


def assert_path_in_sys_path(
		some_path: str | Path | None,
		is_in_sys_path: bool
	) -> None:
	"""
	Verifies whether the presence or absence of the given path in list sys.path
	matches what is expected.

	Args:
		some_path: the path to a directory.
		is_in_sys_path: whether the presence of some_path in sys.path is
			expected.

	Raises:
		AssertionError: if the presence or absence of some_path in sys.path
			does not match argument is_in_sys_path.
		TypeError: if argument some_path is not None nor an instance of str or
			pathlib.Path.
	"""
	some_path = ensure_path_is_str(some_path, True)
	assert (some_path in sys.path) == is_in_sys_path


def assert_path_is_present(
		some_path: str | Path | None,
		bundle: SysPathBundle,
		is_in_sys_path: bool,
		is_in_bundle: bool
	) -> None:
	"""
	Verifies whether the presence or absence of the given path in list sys.path
	and the given SysPathBundle instance matches what is expected.

	Args:
		some_path: the path to a directory.
		bundle: a SysPathBundle instance.
		is_in_sys_path: whether the presence of some_path in sys.path is
			expected.
		is_in_bundle: whether the presence of some_path in the bundle is
			expected.

	Raises:
		AssertionError: if the presence or absence of some_path in sys.path
			or the bundle does not match arguments is_in_sys_path and
			is_in_bundle.
		TypeError: if argument some_path is not None nor an instance of str or
			pathlib.Path.
	"""
	some_path = ensure_path_is_str(some_path, True)
	assert (some_path in sys.path) == is_in_sys_path
	assert bundle.contains(some_path) == is_in_bundle


def index_in_sys_path(some_path: str | Path | None) -> int:
	"""
	Indicates the index of the given path in list sys.path.

	Args:
		some_path: the path to a directory.

	Returns:
		int: the index of some_path in list sys.path.

	Raises:
		ValueError: if some_path is not in sys.path.
	"""
	some_path = ensure_path_is_str(some_path, True)
	return sys.path.index(some_path)


__all__ = [
	"INIT_SYS_PATH",
	"TEST_DIR",
	"REPO_ROOT",
	"LIB_DIR",
	assert_path_in_sys_path.__name__,
	assert_path_is_present.__name__,
	index_in_sys_path.__name__,
	reset_sys_path.__name__
]

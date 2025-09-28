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


def index_in_sys_path(some_path: str | Path) -> int:
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


def reset_sys_path() -> None:
	"""
	Assigns a copy of INIT_SYS_PATH to sys.path.
	"""
	# Copying the list is necessary to preserve the initial state.
	sys.path = list(INIT_SYS_PATH)


__all__ = [
	"INIT_SYS_PATH",
	"TEST_DIR",
	"REPO_ROOT",
	"LIB_DIR",
	index_in_sys_path.__name__,
	reset_sys_path.__name__
]

# __all__ declared at the module's end

from pathlib import Path
import sys


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


__all__ = [
	"INIT_SYS_PATH",
	"TEST_DIR",
	"REPO_ROOT",
	"LIB_DIR",
	reset_sys_path.__name__
]

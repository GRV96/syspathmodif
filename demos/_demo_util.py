from pathlib import Path
import sys


_NEW_LINE = "\n"

INIT_SYS_PATH = list(sys.path)
"""
The initial content of sys.path.
"""

DEMO_DIR = Path(__file__).resolve().parent
"""
The demos' directory
"""

REPO_ROOT = DEMO_DIR.parent
"""
This repository's root directory
"""


def print_sys_path(message: str) -> None:
	"""
	Prints a message then the items in sys.path on separate lines.

	Args:
		message: a message to display above sys.path's items.
	"""
	print(message + _NEW_LINE + _NEW_LINE.join(sys.path))


def reset_sys_path() -> None:
	"""
	Assigns a copy of INIT_SYS_PATH to sys.path.
	"""
	sys.path = list(INIT_SYS_PATH)

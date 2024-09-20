from pathlib import Path
import sys


_SYS_PATH = sys.path


def sp_append(some_path):
	pass


def sp_contains(some_path):
	pass


def sp_remove(some_path):
	pass


def _ensure_path_is_str(some_path):
	if isinstance(some_path, str):
		return some_path
	elif isinstance(some_path, Path):
		return str(some_path)
	else:
		raise TypeError("A path must be of type str or pathlib.Path.")

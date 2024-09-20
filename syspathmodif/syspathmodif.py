from pathlib import Path
import sys


_SYS_PATH = sys.path


def sp_append(some_path):
	some_path = _ensure_path_is_str(some_path)
	_SYS_PATH.append(some_path)


def sp_contains(some_path):
	some_path = _ensure_path_is_str(some_path)
	return some_path in _SYS_PATH


def sp_remove(some_path):
	some_path = _ensure_path_is_str(some_path)
	_SYS_PATH.remove(some_path)


def _ensure_path_is_str(some_path):
	if isinstance(some_path, str):
		return some_path
	elif isinstance(some_path, Path):
		return str(some_path)
	else:
		raise TypeError("A path must be of type str or pathlib.Path.")

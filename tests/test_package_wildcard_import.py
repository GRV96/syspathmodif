import pytest

from pathlib import Path
import sys


# syspathmodif's users are not supposed to directly use the packages' modules.
# These tests ensure that the wildcard import does not include them.

# Since wildcard imports are not allowed within classes and functions,
# the tests perform them with exec.


_REPO_ROOT = str(Path(__file__).resolve().parents[1])


def test_module_import_demo_package():
	sys.path.append(_REPO_ROOT)
	exec("from demo_package import *")
	sys.path.remove(_REPO_ROOT)

	with pytest.raises(NameError, match=".*_ajxo.*"):
		_ajxo

	with pytest.raises(NameError, match=".*_point.*"):
		_point


def test_module_import_syspathmodif():
	sys.path.append(_REPO_ROOT)
	exec("from syspathmodif import *")
	sys.path.remove(_REPO_ROOT)

	with pytest.raises(NameError, match=".*_syspathmodif.*"):
		_syspathmodif

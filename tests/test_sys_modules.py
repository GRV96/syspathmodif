from pathlib import Path
import sys


_LOCAL_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _LOCAL_DIR.parent


sys.path.append(str(_REPO_ROOT))
from syspathmodif import\
	sm_contains,\
	sp_remove
sp_remove(_REPO_ROOT)


def test_sm_contains_int():
	assert not sm_contains(17)


def test_sm_contains_none():
	assert not sm_contains(None)


def test_sm_contains_pathlib():
	assert sm_contains("pathlib")


def test_sm_contains_sys():
	assert sm_contains("sys")


def test_sm_contains_syspathmodif():
	assert sm_contains("syspathmodif")


def test_sm_contains_strath():
	# strath is a dependency of syspathmodif.
	assert sm_contains("strath")

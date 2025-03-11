"""
This script is meant to run on GitHub's virtual machine ubuntu-latest in a CI
workflow.

If a bundle is cleared by the destructor when the application ends, sys.path
can be None, which causes an AttributeError. This script's success ensures that
the exception is properly handled.
"""


from pathlib import Path
import sys


_LOCAL_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _LOCAL_DIR.parents[1]
_LIB_DIR = _REPO_ROOT/"syspathmodif"


sys.path.insert(0, str(_REPO_ROOT))
from syspathmodif import\
	SysPathBundle,\
	sp_remove
sp_remove(_REPO_ROOT)

bundle = SysPathBundle((_LOCAL_DIR, _REPO_ROOT, _LIB_DIR), True)
print(repr(bundle))

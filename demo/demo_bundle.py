from pathlib import Path
import sys


_NEW_LINE = "\n"


def _print_sys_path(title):
	print(title + _NEW_LINE + _NEW_LINE.join(sys.path))


_INIT_SYS_PATH = list(sys.path)
_print_sys_path("Initial sys.path content")

_LOCAL_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _LOCAL_DIR.parent
_PACKAGE_DIR = _REPO_ROOT/"demo_package"
print(f"\nLocal directory: {_LOCAL_DIR}")
print(f"Repository root: {_REPO_ROOT}")
print(f"Package: {_PACKAGE_DIR}")


# syspathmodif is imported here.
sys.path.append(str(_REPO_ROOT))

_print_sys_path(
	"\nRepository root appended to sys.path to import package syspathmodif")

from syspathmodif import\
	SysPathBundle,\
	sp_contains

sys.path = list(_INIT_SYS_PATH)
_print_sys_path("\nsys.path reset after the importation")
# End of syspathmodif's importation


# syspathmodif is used here.
print(f"\nsys.path contains the repository's root: {sp_contains(_REPO_ROOT)}")
print(f"sys.path contains the package's directory: {sp_contains(_PACKAGE_DIR)}")

bundle = SysPathBundle((_REPO_ROOT, _PACKAGE_DIR))
_print_sys_path(
	"\nPaths appended to sys.path to import from demo_package")

from demo_package import Ajxo
from _point import Point

print(f"\nsys.path contains the repository's root: {sp_contains(_REPO_ROOT)}")
print(f"sys.path contains the package's directory: {sp_contains(_PACKAGE_DIR)}")

# Paths removed by __del__ when the garbage collector destroys the bundle.
del bundle
_print_sys_path(
	"\nPaths removed from sys.path after the imports")

print(f"\nsys.path contains the repository's root: {sp_contains(_REPO_ROOT)}")
print(f"sys.path contains the package's directory: {sp_contains(_PACKAGE_DIR)}")
# End of syspathmodif's use


ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

print("\nsys.path is the same as before the demo: "\
		+ str(sys.path == _INIT_SYS_PATH))

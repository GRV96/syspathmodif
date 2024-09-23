from pathlib import Path
import sys


_NEW_LINE = "\n"


def _print_sys_path(title):
	print(title + _NEW_LINE + _NEW_LINE.join(sys.path))


_INIT_SYS_PATH = list(sys.path)
_print_sys_path("Initial sys.path content")

_LOCAL_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _LOCAL_DIR.parent


# syspathmodif is imported here.
sys.path.append(str(_REPO_ROOT))
_print_sys_path(
	"\nRepository root appended to sys.path to import package syspathmodif")
from syspathmodif import\
	sp_append,\
	sp_contains,\
	sp_remove
sys.path = list(_INIT_SYS_PATH)
_print_sys_path("\nsys.path reset after the importation")
# End of syspathmodif's importation


# syspathmodif is used here.
print(f"\nsys.path contains the repository's root: {sp_contains(_REPO_ROOT)}")
sp_append(_REPO_ROOT)
_print_sys_path(
	"\nRepository root appended to sys.path to import demo_package")
from demo_package import\
	Ajxo,\
	Point
print(f"\nsys.path contains the repository's root: {sp_contains(_REPO_ROOT)}")
sp_remove(_REPO_ROOT)
_print_sys_path(
	"\nRepository root removed from sys.path after the importation")
print(f"\nsys.path contains the repository's root: {sp_contains(_REPO_ROOT)}")
# End of syspathmodif's use


ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

print("\nsys.path is the same as before the demo: "\
		+ str(sys.path == _INIT_SYS_PATH))

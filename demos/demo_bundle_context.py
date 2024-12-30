import sys

from _demo_util import\
	INIT_SYS_PATH,\
	DEMO_DIR,\
	REPO_ROOT,\
	print_sys_path,\
	reset_sys_path


_PACKAGE_DIR = REPO_ROOT/"demo_package"

print_sys_path("sys.path's initial content")

print(f"\nDemo directory: {DEMO_DIR}")
print(f"Repository root: {REPO_ROOT}")
print(f"Package: {_PACKAGE_DIR}")


# Imports from syspathmodif are performed here.
sys.path.append(str(REPO_ROOT))

print_sys_path(
	"\nRepository root appended to sys.path to import package syspathmodif")

from syspathmodif import\
	SysPathBundle,\
	sp_contains

reset_sys_path()
print_sys_path("\nsys.path reset after the importation")
# End of imports from syspathmodif


# SysPathBundle is used here.
print(f"\nsys.path contains the repository's root: {sp_contains(REPO_ROOT)}")
print(f"sys.path contains the package's directory: {sp_contains(_PACKAGE_DIR)}")

# The bundle adds the paths to sys.path. The block's end clears the bundle.
with SysPathBundle((REPO_ROOT, _PACKAGE_DIR)):
	print_sys_path(
		"\nPaths appended to sys.path to import from demo_package")

	from demo_package import Ajxo
	from point import Point

	print(f"\nsys.path contains the repository's root: {sp_contains(REPO_ROOT)}")
	print(f"sys.path contains the package's directory: {sp_contains(_PACKAGE_DIR)}")

print_sys_path(
	"\nPaths removed from sys.path after the imports")

print(f"\nsys.path contains the repository's root: {sp_contains(REPO_ROOT)}")
print(f"sys.path contains the package's directory: {sp_contains(_PACKAGE_DIR)}")
# End of SysPathBundle's use


ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

is_sys_path_the_same = sys.path == INIT_SYS_PATH
print(f"\nsys.path is the same as before the demo: {is_sys_path_the_same}")
assert is_sys_path_the_same

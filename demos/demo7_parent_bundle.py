import sys

from _demo_utils import\
	INIT_SYS_PATH,\
	REPO_ROOT,\
	print_sys_path,\
	reset_sys_path


print_sys_path("sys.path's initial content")

print(f"\nRepository root: {REPO_ROOT}")


# Imports from syspathmodif are performed here.
sys.path.insert(0, str(REPO_ROOT))
print_sys_path(
	"\nRepository root prepended to sys.path to import package syspathmodif")

from syspathmodif import\
	sp_contains,\
	sp_prepend_parent_bundle

reset_sys_path()
print_sys_path("\nsys.path reset after the importation")
# End of imports from syspathmodif


# syspathmodif is used here.
print(f"\nsys.path contains the repository's root: {sp_contains(REPO_ROOT)}")

# The SysPathBundle contains the repository's root.
with sp_prepend_parent_bundle((1,)):
	print_sys_path(
		"\nRepository root prepended to sys.path to allow imports")

	from demo_package import Ajxo, Point

	print(f"\nsys.path contains the repository's root: {sp_contains(REPO_ROOT)}")

print(f"\nsys.path contains the repository's root: {sp_contains(REPO_ROOT)}")
# End of syspathmodif's use


ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

is_sys_path_the_same = sys.path == INIT_SYS_PATH
print(f"\nsys.path is the same as before the demo: {is_sys_path_the_same}")
assert is_sys_path_the_same

from pathlib import Path
import sys

from _demo_utils import\
	INIT_SYS_PATH,\
	DEMO_DIR,\
	REPO_ROOT,\
	print_sys_path,\
	reset_sys_path


print_sys_path("sys.path's initial content")

print(f"\nDemo directory: {DEMO_DIR}")
print(f"Repository root: {REPO_ROOT}")


# Imports from syspathmodif are performed here.
sys.path.insert(0, str(REPO_ROOT))
print_sys_path(
	"\nRepository root prepended to sys.path to import package syspathmodif")

from syspathmodif import\
	sp_contains,\
	sp_prepend_parent,\
	sp_remove

reset_sys_path()
print_sys_path("\nsys.path reset after the importation")
# End of imports from syspathmodif


# syspathmodif is used here.
print(f"\nsys.path contains the repository's root: {sp_contains(REPO_ROOT)}")

repo_root = sp_prepend_parent(1)
if repo_root == REPO_ROOT:
	print_sys_path(
		"\nRepository root prepended to sys.path to import from demo_package")

from demo_package import\
	Ajxo,\
	Point

print(f"\nsys.path contains the repository's root: {sp_contains(repo_root)}")

if sp_remove(repo_root):
	print_sys_path(
		"\nRepository root removed from sys.path after the import")

print(f"\nsys.path contains the repository's root: {sp_contains(repo_root)}")
# End of syspathmodif's use


ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

is_sys_path_the_same = sys.path == INIT_SYS_PATH
print(f"\nsys.path is the same as before the demo: {is_sys_path_the_same}")
assert is_sys_path_the_same

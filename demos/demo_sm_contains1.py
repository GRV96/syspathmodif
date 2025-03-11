import sys

from _demo_util import\
	REPO_ROOT


sys.path.append(str(REPO_ROOT))
from syspathmodif import\
	SysPathBundle,\
	sm_contains,\
	sp_prepend,\
	sp_remove
sp_remove(REPO_ROOT)


def _add_demo_package_to_sys_modules():
	was_repo_root_added = sp_prepend(REPO_ROOT)

	# The import includes the package in sys.modules.
	import demo_package

	if was_repo_root_added:
		sp_remove(REPO_ROOT)


paths = list()

# This function call prevents the first conditional block's execution.
# Comment it out and see the result.
_add_demo_package_to_sys_modules()

# To import Ajxo
if not sm_contains("demo_package"):
	print("Repository's root added to sys.path")
	paths.append(REPO_ROOT)

# To import Point
if not sm_contains("point"):
	print("Directory demo_package added to sys.path")
	paths.append(REPO_ROOT/"demo_package")

with SysPathBundle(paths):
	from demo_package import Ajxo
	from point import Point

ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

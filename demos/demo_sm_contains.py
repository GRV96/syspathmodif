import sys

from _demo_util import\
	REPO_ROOT


sys.path.append(str(REPO_ROOT))
from syspathmodif import\
	SysPathBundle,\
	sm_contains,\
	sp_remove
sp_remove(REPO_ROOT)


paths = list()

# To import Ajxo
if not sm_contains("demo_package"):
	print("Repository's root added to sys.path")
	paths.append(REPO_ROOT)

# To import Point
if not sm_contains("point"):
	print("demo_package added to sys.path")
	paths.append(REPO_ROOT/"demo_package")

with SysPathBundle(paths):
	from demo_package import Ajxo
	from point import Point

ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

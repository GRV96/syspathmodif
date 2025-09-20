import sys

from _demo_utils import\
	REPO_ROOT


sys.path.insert(0, str(REPO_ROOT))
from syspathmodif import\
	sm_contains,\
	sp_append,\
	sp_remove

# This import adds demo_package to sys.modules.
# Comment it out and see the result.
import demo_package
sp_remove(REPO_ROOT)


was_repo_root_added = False
if not sm_contains("demo_package"):
	was_repo_root_added = sp_append(REPO_ROOT)
	print(f"Repository root appended to sys.path: {was_repo_root_added}")

from demo_package import\
	Ajxo,\
	Point
print("Classes imported from demo_package")

if was_repo_root_added:
	was_repo_root_removed = sp_remove(REPO_ROOT)
	print(f"Repository root removed from sys.path: {was_repo_root_removed}")

ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

"""
This demo imitates a situation where prepending directory paths to sys.path is
optional. Argument --paths allows the user to instantiate a SysPathBundle with
the content of their choice.

--paths is omitted: the content is None.

--paths has no values: the content is an empty tuple.

--paths has one or more values: the content is a tuple of paths.
"""


from argparse import\
	ArgumentParser, RawDescriptionHelpFormatter
import os
import sys

from _demo_utils import\
	INIT_SYS_PATH,\
	REPO_ROOT,\
	print_sys_path,\
	reset_sys_path


sys.path.insert(0, str(REPO_ROOT))
from syspathmodif import SysPathBundle
reset_sys_path()


arg_parser = ArgumentParser(
	description=__doc__,
	formatter_class=RawDescriptionHelpFormatter
)
arg_parser.add_argument(
	"--paths", nargs="*", required=False,
	help="Paths to prepend to sys.path with SysPathBundle. Default: None."
)
args = arg_parser.parse_args()
paths: tuple[str, ...] | None = (
	None if args.paths is None
	else tuple(os.path.abspath(p) for p in args.paths)
)


print_sys_path("sys.path's initial content:")

bundle = SysPathBundle(paths, True)
print("\nBundle instantiated with these paths:")
print("\n".join(paths) if paths else paths)
print_sys_path("\nPaths prepended to sys.path to import from demo_package.")

were_imports_successful: bool = False
try:
	from demo_package import Ajxo
	from point import Point
	print("\nImports performed.")
	were_imports_successful = True
except ImportError:
	pass

del bundle
print_sys_path(
	"\nPaths removed from sys.path on the bundle's deletion.")

if not were_imports_successful:
	print("\nERROR! The imports failed.")
	sys.exit(1)


ajxo = Ajxo("a string", [7, 11, 13])
point = Point(41, 97)

print("\nInstances of imported classes")
print(ajxo)
print(point)

is_sys_path_the_same = sys.path == INIT_SYS_PATH
print(f"\nsys.path is the same as before the demo: {is_sys_path_the_same}")
assert is_sys_path_the_same

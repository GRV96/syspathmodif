#!/bin/python3

from os import system
from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parents[2]


# This script builds the PyPI package and installs it to ensure the
# installation works. However, the script does not upload the package to PyPI.

system(f"python3 {_REPO_ROOT}/setup.py sdist")

latest_dist = list((_REPO_ROOT/"dist").glob("syspathmodif-*.tar.gz"))[-1]

system(f"pip3 install --no-cache-dir {latest_dist}")


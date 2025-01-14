"""
This script is meant to run on GitHub's virtual machine ubuntu-latest in a CI
workflow. It builds the PyPI package and installs it to ensure the
installation works. However, the script does not upload the package to PyPI.
"""


from os import system
from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parents[2]


system(f"python3 {_REPO_ROOT}/setup.py sdist")

latest_dist = next((_REPO_ROOT/"dist").glob("syspathmodif-*.tar.gz"))

system(f"pip3 install --no-cache-dir {latest_dist}")

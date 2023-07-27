from os import chdir
from pathlib import Path


def create_dir(name_dir: str):
    name = Path(
        Path.cwd() / name_dir)
    if not name.exists():
        name.mkdir()
    chdir(name)


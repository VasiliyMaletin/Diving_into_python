from create_file import create_file
import os


def gen_files(direct: str, data: dict):
    os.chdir(direct)
    for key, value in data.items():
        create_file(key, amount_file=value)

import my_build
from .. import module_path
from os.path import join
import os


def hello2():
    print("hello2")


def my_file():
    with open(os.path.join(module_path, 'data/a.txt')) as f:
        print(f.readlines())

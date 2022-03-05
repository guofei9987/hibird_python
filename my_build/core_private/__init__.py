import os
import ctypes

from . import CoreClass  # import python .so

core_path = os.path.dirname(__file__)

core_files = os.listdir(core_path)

so_files = dict()
for file in core_files:
    if file.endswith('.so'):
        prefix = file.split('.')[0]
        so_files[prefix] = file



# read C so
CoreFunction = ctypes.cdll.LoadLibrary(os.path.join(
    core_path
    , so_files['CoreFunction']
))

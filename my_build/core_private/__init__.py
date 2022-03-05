import os
import ctypes

# python 生成的 .so 文件，这样引入：
from . import CoreClass  # import python .so

# C生成的 .so 文件，这样引入
core_path = os.path.dirname(__file__)

so_files = {file.split('.')[0]: os.path.join(core_path, file)
            for file in os.listdir(core_path)
            if file.endswith('.so')}

# read .so
CoreFunction = ctypes.cdll.LoadLibrary(so_files['CoreFunction'])

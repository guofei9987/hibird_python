import os
import ctypes

core_path = os.path.dirname(__file__)

core_files = os.listdir(core_path)

so_files = {file.split('.')[0]: os.path.join(core_path, file)
            for file in core_files
            if file.endswith('.so')}

# read .so
CoreFunction = ctypes.cdll.LoadLibrary(so_files['CoreFunction'])

# 编译 py 文件，编译 c 文件。执行：
# python setup.py build_ext  --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["CoreClass.py", 'CoreFunction.c']))

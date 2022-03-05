# 如果不想打包源码，把这个文件夹复制出去，并执行：
# python setup.py build_ext  --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["CoreClass.py", 'CoreFunction.c']))

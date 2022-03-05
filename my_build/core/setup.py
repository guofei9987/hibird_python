# 执行这个来生成 .so 文件，方便本地测试
# python setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(['CoreFunction.c']))

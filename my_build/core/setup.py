# 如果是打包整个项目，用不到本文件。
# 因为在用户 pip install 的时候，会根据 ./setup.py 的信息，编译本目录中的 C 源文件
# 仍然保留本文件，是因为在本地测试而非 pip install，同样需要编译
# 执行下面的代码来编译 C 源文件
# python setup.py build_ext --inplace
# 编译完成后可能需要从 /build 文件夹中把 so 文件复制到本目录（根据平台不同，有的直接就在本目录了）
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(['CoreFunction.c']))

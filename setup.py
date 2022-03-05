from setuptools import setup
from setuptools import find_packages

# from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

#
setup(
    name='my_build',  # 包的名字，也是将来用户使用 pip install scikit-opt 来安装
    version='0.0.1',  # 版本号，每次上传的版本号应当不一样，可以用类似 sko.__version__ 去自动指定
    python_requires='>=3.5',
    packages=['my_build', 'my_build.sub'],
    ext_modules=[
        # c文件会编译为 .so 文件
        Extension(
            # 1)必须指定my_build，否则 so 文件直接生成到包的根目录下。
            # 2）my_add 是生成的so文件名，会自动添加后缀使其符合规范
            "my_build.my_add",
            # 被编译的 c 文件
            ['my_build/my_add.c', 'my_build/my_add2.c'])
    ],

    # ext_modules=cythonize('my_build/hello.py')

    package_data={'my_build': ['data/*.txt']}
    # ext_modules=cythonize("my_build/hello.py")
    # data_files=[('my_build', ['my_build/data/*.txt'])]

)

from setuptools import setup
from setuptools import find_packages

# from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

print("installing my_build, it is an example for python extension!")

# 完全开源
setup(
    name='my_build',
    version='0.0.2',  # 版本号，每次上传的版本号应当不一样，可以用类似 sko.__version__ 去自动指定
    python_requires='>=3.5',
    packages=['my_build', 'my_build.sub', 'my_build.core'],  # 这里不加入 my_build.core
    ext_modules=[
        # c文件会编译为 .so 文件
        Extension(
            # 1)必须指定my_build，否则 so 文件直接生成到包的根目录下。
            # 2）my_add 是生成的so文件名，会自动添加后缀使其符合规范
            "my_build.core.CoreFunction",
            # 被编译的 c 文件
            ['my_build/core/CoreFunction.c'])
    ],

    # ext_modules=cythonize('my_build/hello.py')

    package_data={'my_build': ['data/*.txt']},
    # data_files=[('my_build', ['my_build/data/*.txt'])]

)

#
# # 核心保密：
# setup(
#     name='my_build',
#     version='0.0.2',  # 版本号，每次上传的版本号应当不一样，可以用类似 sko.__version__ 去自动指定
#     python_requires='>=3.5',
#     packages=['my_build', 'my_build.sub', 'my_build.core'],  # 这里不加入 my_build.core
#     # ext_modules=[
#     #     # c文件会编译为 .so 文件
#     #     Extension(
#     #         # 1)必须指定my_build，否则 so 文件直接生成到包的根目录下。
#     #         # 2）my_add 是生成的so文件名，会自动添加后缀使其符合规范
#     #         "my_build.my_add",
#     #         # 被编译的 c 文件
#     #         ['my_build/my_add.c', 'my_build/my_add2.c'])
#     # ],
#
#     # ext_modules=cythonize('my_build/hello.py')
#
#     package_data={'my_build': ['data/*.txt', 'core/__init__.py']},
#     ext_modules=cythonize(["my_build/core/CoreClass.py", 'my_build/core/CoreFunction.c'])
#     # data_files=[('my_build', ['my_build/data/*.txt'])]
#
# )

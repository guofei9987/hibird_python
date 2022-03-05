# tst-data
from my_build import hello
from my_build.sub import hello2

hello.say_hello()

hello2.hello2()

print("read_file res:")
hello2.my_file()

# %% 测试公开 c 文件编译（先生成so文件，然后运行此段代码）

from my_build import core

c_res = core.CoreFunction.my_func(1, 3)
print('c_res', c_res)


#%% 测试加密 c和python 文件编译（也是先生成，然后运行此段代码）
from my_build import core_private

c_res = core_private.CoreFunction.my_func(1, 3)
print('private c_res', c_res)

core_class = core_private.CoreClass.MyClass()
py_res = core_class.my_add(1, 2)
print('private py_res=', py_res)

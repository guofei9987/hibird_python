# tst-data
from my_build import hello
from my_build.sub import hello2

hello.say_hello()

hello2.hello2()

print("read_file res:")
hello2.my_file()

# %%
# tst-so

from my_build import core

c_res = core.CoreFunction.my_func(1, 3)
print('c_res', c_res)

core_class = core.CoreClass.MyClass()
py_res = core_class.my_add(1, 2)
print('py_res=', py_res)

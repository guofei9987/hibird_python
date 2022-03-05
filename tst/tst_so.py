from my_build import core

c_res = core.CoreFunction.my_func(1, 3)
print('c_res', c_res)

core_class = core.CoreClass.MyClass()
py_res = core_class.my_add(1, 2)
print('py_res=', py_res)

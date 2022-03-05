import ctypes


def say_hello():
    print("hello world")


def get_my_so():
    my_so = ctypes.cdll.LoadLibrary("my_add.cpython-38-darwin.so")
    return my_so


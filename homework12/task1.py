import time
def my_func(func):
    def my_function():
        print("function start time, and function name:")
        func()
        print("decorator end")
    return my_function()

@my_func
def func():
    print(time.ctime())
    print(my_func.__name__)
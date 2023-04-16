import time
def my_func(func):
    def my_function():
        print("function start time, and function name:")
        func()
        print(func.__name__)
        print("decorator end")
    return my_function()

@my_func
def My_func1():
    print(time.ctime())
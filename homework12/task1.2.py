import time
def my_func(func):
    def my_function():
        print(f"function start time: {time.ctime()} and function name:")
        print(func.__name__)
        func()
    return my_function()

@my_func
def My_func1():
    print("decorator end")
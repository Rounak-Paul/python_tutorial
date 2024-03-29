# decorators in Python

# syntax
# @decorator
# def <my_func>():
#   <logic>

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

import time

def timeit(func):
    def wrapper():
        t_start = time.time()
        func()
        print(f"ex time (s): {time.time() - t_start}")
    return wrapper

@timeit
def mul():
    for i in range(10000000):
        i*i

mul()
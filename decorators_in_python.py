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
    def wrapper(temp):
        t_start = time.time()
        i = func(temp)
        print(f"ex time (s): {time.time() - t_start}")
        return i
    return wrapper

n = 100000000

@timeit
def mul(val):
    for i in range(val):
        i*i
    return i

last_val = mul(n)
print(last_val)
# function in python

# why we need functions - 2 main reasons
# 1. write modular logic which can be reused and compact
# 2. abstract the implementation

# you are already using functions

print("anything") # print is a function

# syntax
# def <function_name>():
#   <function_logic>
#   return

'''
def ->  this is the keyword to let python know
        that the following name is a function

<function_name> ->  this unique name can be used 
                    to call the function

<function_logic> -> this logic will be executed
                    when the function is called

return ->   the statement to end and return a
            value
'''

def my_function():
    print("Hello, from my_function")
    return

my_function()

# arguments in function
def add_nums(num1, num2):
    output = num1 + num2
    print(output)
    return

add_nums(5, 10)

# return value
def add_nums(num1, num2):
    output = num1 + num2
    return output

answer = add_nums(2, 4)
print(answer)

def show_2nd_num(num1, num2):
    print(num2)
    return

show_2nd_num(1, 2)
show_2nd_num(num2=1, num1=1)

def many_args(*args):
    print(type(args)) # args is tuple
    print(args)
    print(args[-1]) # indexing over args
    return

many_args(1,2,3,4,5)
many_args(1,2,3,4,5,6,7,8,9)

def many_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["name"])
    return

many_kwargs(name="rounak", age=6000, likes="relax")

def s_mult(vector, k=6):
    for i in range(len(vector)):
        vector[i] *= k
    return vector

print(s_mult([3,4,5], k=0))
print(s_mult([3,4,5]))




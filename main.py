# Variables

x = 5
y = "Duke"

print(x)
print(y)

# Names can be anything without space/ not starting with number/ not containing math_symbols
# Examples of not valid names: 
# 2name0fvar = 123
# my-var = "abc"
# my var = 12

# Python Built in Data Types

x_str = "Hello" # str
print(x_str + " is " + type(x))

x_int = 2 # int
print(x_int + " is " + type(x_int))

x_float = 10.2 # float
print(x_float + " is " + type(x_float))

x_complex = 1j # complex
print(x_complex + " is " + type(x_complex))

x_list = [1, 2, 3, 4] # list
print(x_list + " is " + type(x_list))

x_tuple = (1, 2, 3, 4) # tuple
print(x_tuple + " is " + type(x_tuple))

x_range = range(6) # range
print(x_range + " is " + type(x_range))

x_dict = { # dict
    "name" : "Duke",
    "age" : 23
}
print(x_dict + " is " + type(x_dict))

x_set = set({"a", "b", "c", "a"}) # set
print(x_set + " is " + type(x_set))

x_bool = True # bool
print(x_bool + " is " + type(x_bool))

x_bytes = b"Hello" # bytes
print(x_bytes + " is " + type(x_bytes))

x_none = None # None
print(f"{x_none} is {type(x_none)}")

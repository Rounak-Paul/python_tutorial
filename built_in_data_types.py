# Python Built in Data Types

x_str = "Hello" # str
print(f"{x_str} is {type(x_str)}")

x_int = 2 # int
print(f"{x_int} is {type(x_int)}")

x_float = 10.2 # float
print(f"{x_float} is {type(x_float)}")

x_complex = 1j # complex
print(f"{x_complex} is {type(x_complex)}")

x_list = [1, 2, 3, 4] # list
print(f"{x_list} is {type(x_list)}")

x_tuple = (1, 2, 3, 4) # tuple
print(f"{x_tuple} is {type(x_tuple)}")

x_range = range(6) # range
print(f"{x_range} is {type(x_range)}")

x_dict = { # dict
    "name" : "Duke",
    "age" : 23
}
print(f"{x_dict} is {type(x_dict)}")

x_set = set({"a", "b", "c", "a"}) # set
print(f"{x_set} is {type(x_set)}")

x_bool = True # bool
print(f"{x_bool} is {type(x_bool)}")

x_bytes = b"Hello" # bytes
print(f"{x_bytes} is {type(x_bytes)}")

x_none = None # None
print(f"{x_none} is {type(x_none)}")

# Multiple assignment
a, b, c = (10, 20, 30)
print(f'a={a}, b={b}, c={c}')

# type casting

# int() -> construct int from integer literal/ float literal(removes the decimals)/ string literal of whole numbers

x = int(1)
y = int(12.2)
z = int("20")

print(f'x={x} is type of {type(x)}')
print(f'x={y} is type of {type(y)}')
print(f'x={z} is type of {type(z)}')

# float() -> construct float from float literal/ string literal of float number
x = float(88.9)
y = float("23.5")

print(f'x={x} is type of {type(x)}')
print(f'x={y} is type of {type(y)}')

# str() -> construct string from a wide range of types
x = str(2)
y = str(23.5)
z = str("a string")

print(f'x={x} is type of {type(x)}')
print(f'x={y} is type of {type(y)}')
print(f'x={z} is type of {type(z)}')

############################ String ##############################
# string format
name = "Duke"
age = 23
likes = "games"

f_string = f"Name: {name}, Age: {age}, Likes: {likes}"

print(f_string)

f_string = "Name: {0}, Age: {1}, Likes: {2}".format(name, age, likes)
print(f_string)

# another way to init string
a_str = """
kahbdadwlaj
awdijalkwdm
apwdjlawd
poawidpoakdo
"""

print(a_str)

# strings are indexed

a_str = "this is a very long string"

print(a_str[0:-1]) # does not include the -1th index

str_of_numbers = "0123456789"

print(str_of_numbers[0:3]) # for indexing [a: b], a is inclusive but b is exclusive

print(str_of_numbers[0:8:2]) # from "01234567" we are picking every 2nd entry

# slicing [a_included: b_excluded: step_size]

for i in str_of_numbers:
    print(i)

# Modify string
a_str = "        This, is a very, Long String         "

print(a_str.upper())
print(a_str.lower())
print(a_str.strip())

print(a_str.replace("s", "p"))

print(a_str.split(",")) # returns a list

# example of chain use
modified_a_str = a_str.upper().strip().replace("i", "x").split(",")

print(modified_a_str)

# concat strings

a = "String 1"
b = "String 2"

print(a + ", " + b)

############################ Booleans ##############################

a = True
print(a)

print(1 == 2) # == is for comparison, not assignment

print( 10 > 2)

print(bool("Hello"))
print(bool("")) # with this bool typecast we can check if string is empty or not

############################ Numbers ##############################
a = 20
b = 30

print("Numbers")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b % a)
print(a ** b) # a to the power b,  a^b
print(b // 16) # floor division, rounds the result to nearest whole number


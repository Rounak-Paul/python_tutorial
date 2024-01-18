# if ... else & match ... case in Python

# Comparison operators
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 10
b = 11

print(a == b)  # False
print(a != b)  # True
print(a < b)   # True
print(a <= b)  # True
print(a > b)   # False
print(a >= b)  # False

# syntax
# if <condition>:
#   <logic_1>
# else:
#   <logic_2>

a = 10
b = 20

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# only if conditions

if a == 0:
    print("a is equal to 10")

if b > 10:
    print("b is greater than 10")


# elif condition
if a == 0:
    print("a is 10")
elif b == 20:
    print("b is 10")
else:
    print("no match")

# match case **Python 3.10+
match a:
    case 20:
        print("a is 20")
    case 10:
        print("a is 10")

# shorthand if ... else
# logic_1 if condition else logic_2
print("logic_1") if a < b else print("logic_2")




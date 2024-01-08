# Tuple in python

my_tuple = ("apple", 99, "ball", 99, True, "mouse", 'ball', 99)
print(f"{my_tuple} is of type {type(my_tuple)}")

# List is written with []
# Tuple is written with () 

###### Why tuple if different from list ######
# Tuple is IMMUTABLE, which means values of a touple can not be changed.
# You can assign some other tuple to the same variable name, but you can 
# change values of a touple.

# my_tuple[2] = 'cat' # TypeError: 'tuple' object does not support item assignment

index_of_element = my_tuple.index('ball') 
print(index_of_element)

count_of_element = my_tuple.count('ball')
print(count_of_element)

new_tuple = ('pink', 68, 'tree', 70)

# addition of tuples
combined_tuple = my_tuple + new_tuple
print(my_tuple)
print(new_tuple)
print(combined_tuple)

# unpacking
a1, a2, a3, a4 = new_tuple
print(a1)

list_of_new_tuple = []
list_of_new_tuple[:] = new_tuple
print(list_of_new_tuple)

list_typecast_of_tuple = list(new_tuple)
print(f"{list_typecast_of_tuple} is of type {type(list_typecast_of_tuple)}")

# unpacking unknown number of items
# add * before the variable name to contain the rest of the items in a list
item1, item2, *others = my_tuple
print(f"{item1} is of type {type(item1)}") # apple is of type <class 'str'>
print(f"{item2} is of type {type(item2)}") # 99 is of type <class 'int'>
print(f"{others} is of type {type(others)}") # ['ball', 99, True, 'mouse', 'ball', 99] is of type <class 'list'>


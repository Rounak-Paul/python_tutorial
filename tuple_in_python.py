# Tuple in python

# Define a Tuple
my_tuple = ("apple", 99, "ball", 99, True, "mouse", "ball", 99)
print(f"{my_tuple} is of type {type(my_tuple)}") # <class 'tuple'>

###### Why Tuple is different from List ######
# Tuple is IMMUTABLE, which means values of a tuple can not be changed
# you can assign some other tuple to the same variable name to overwrite it,
# but you can not change a value of tuple

# my_tuple[2] = "cat" # TypeError: 'tuple' object does not support item assignment

index_of_element = my_tuple.index("ball")
print(index_of_element) # 2

count_of_element = my_tuple.count("ball")
print(count_of_element) # 2

count_of_element = my_tuple.count(99)
print(count_of_element) # 3

new_tuple = ("pink", 68, "tree", 70)

# addition of tuples
combined_tuple = my_tuple + new_tuple
print(my_tuple)
print(new_tuple)
print(combined_tuple)
# ('apple', 99, 'ball', 99, True, 'mouse', 'ball', 99)
# ('pink', 68, 'tree', 70)
# ('apple', 99, 'ball', 99, True, 'mouse', 'ball', 99, 'pink', 68, 'tree', 70)

# unpacking ***
a1, a2, a3, a4 = new_tuple
print(a1)
print(a2)
print(a3)
print(a4)

# a1, a2 = new_tuple # ValueError: too many values to unpack (expected 2)

list_of_new_tuple = []
list_of_new_tuple[:] = new_tuple
print(type(list_of_new_tuple)) # <class 'list'>
print(list_of_new_tuple) 

list_of_new_tuple = list(new_tuple)
print(type(list_of_new_tuple)) # <class 'list'>

# unpack unknown number of variables
item1, item2, *others = my_tuple
print(item1)
print(item2)
print(others) # ['ball', 99, True, 'mouse', 'ball', 99]

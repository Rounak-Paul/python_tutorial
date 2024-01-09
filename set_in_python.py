# Set in python

# Duplicates are not allowed in set
my_set = {"apple", 1, 22.5, "Dog", "apple", 22.5, "apple"}
print(my_set)

# Set in Python is UNORDERED, we can not access set element with Index
# my_set[0] # TypeError: 'set' object is not subscriptable

# in set True and 1 are considered as duplicates
# similarly False and 0 are considered as duplicates

a_set = {True, 1, False, 0}
print(a_set)

# length of a set
print(len(my_set))

# Set typecast
# Ex: Get count of unique elements in a list
my_list = ["apple", 1, 22.5, "Dog", "apple", 22.5, "apple"]
print(my_list)
print(len(my_list))
set_of_my_list = set(my_list)
print(set_of_my_list)
print(len(set_of_my_list))

# add item to set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update a set with another iterable
tropical = {"pineapple", "mango", "papaya"}
# tropical = ["dog", "cat"]
thisset.update(tropical)
print(thisset)

# union
tropical = {"pineapple", "mango", "papaya"}
# tropical = ["dog", "cat"]
thisset = thisset.union(tropical)
print(thisset)

# remove
print(thisset)
thisset.remove("banana")
print(thisset)

# discard
thisset.discard("apple")
print(thisset)
# thisset.remove("apple") # KeyError: 'apple'
thisset.discard("apple") # discard will not throw error of the item not in the set

# pop a random element 
x = thisset.pop()
print(thisset)
print(x)

# clear
thisset.clear()
print(thisset)






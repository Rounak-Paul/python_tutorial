# empty list init
amazing_list = []
print(amazing_list)

# list init with value
amazing_list = ['item1', 'item2', 'one_rotten_apple']
print(amazing_list)

# list of multiple data types

amazingly_amazing_list = ['car', 1, False, 2, False, 'car', 'not_a_cat'] # str, int and bool
print(amazingly_amazing_list)

# type of
print(type(amazingly_amazing_list))

# access list items
item_1 = amazingly_amazing_list[0]
print(item_1)
item_1 = amazingly_amazing_list[1]
print(item_1)
item_1 = amazingly_amazing_list[-1]
print(item_1)

# slicing
# slicing is taking a slice of any iterable object
# list[int] is indexing, not slicing
# list[int:] is slicing
# slicing in python returns a list

list1 = [0, 1, 2, 3, 4, 5, 6]

print(list1[0:0]) # returns [], empty list
print(f'{list1[0]} is of type {type(list1[0])}') # int, this is indexing
print(f'{list1[0:1]} is of type {type(list1[0:1])}') # list, this is slicing

# slicing pattern in python
# it is defined as -> iterable[start_index_included : end_index_excluded : step_size]
sliced_list = list1[0:4]
print(f"slice of [0, 4) where 0th index is included and 4th index is excluded: {sliced_list}")

print(f"with step size 2: {list1[2:6:2]}") 

# slicing with empty value
sliced_list = list1[:] # returns list slice from start to finish
print(sliced_list)
print(list1[3:]) # slice starting at 3rd index till the end
print(list1[:3]) # slice starting at begining till 3rd index(not included)

print(list1[::2]) # slice of every 2nd element of the list

# reverse a list in one line
list1_inv = list1[::-1] # slice of every element while counting backwards
print(list1_inv)

# lists are indexed in python
# you can access any element of the list using the respective index
item_0 = list1[0]
print(f'{item_0} is of type {type(item_0)}')
print(f'{list1[4]} is of type {type(list1[4])}')
# index beyond the existing elements count of list can not be accessed and will give an error

# element re-asignment
list1[2] = 'book'
print(list1)

list1[5] = ['tree', 'life']
print(list1) # [0, 1, 'book', 3, 4, ['tree', 'life'], 6], list inside list

# since list1[5] is indexing not slicing but ['tree', 'life'] is a list,
# so the elemt is replaced by the list

list1[5:6] = ['tree', 'life'] # this way, unpacking can take place
print(list1) # [0, 1, 'book', 3, 4, 'tree', 'life', 6]

list1[1:1] = [True, 99, 'of'] # inset unpacked content before 1st index
print(list1) # [0, True, 99, 'of', 1, 'book', 3, 4, 'tree', 'life', 6]

####################### List methods #######################

list1.insert(3, 'mouse') # insert 'mouse' at 3rd index
print(list1) # [0, True, 99, 'mouse', 'of', 1, 'book', 3, 4, 'tree', 'life', 6]

print(list1.pop(3)) # returns item at an index and removes it from list
print(list1) # removed: 'mouse', list: [0, True, 99, 'of', 1, 'book', 3, 4, 'tree', 'life', 6]

# append is inserting new element at the end
list1.append('cheese')
print(list1)

# extend existing list with another iterable, which will be converted to list
l1 = [1,2,3]
l2 = [6,7]
s1 = 'abc'
t1 = (True, 99)

l1.extend(l2)
print(l1) # [1, 2, 3, 6, 7]

l1.extend(s1) 
print(l1) # [1, 2, 3, 6, 7, 'a', 'b', 'c']

l1.extend(t1)
print(l1) # [1, 2, 3, 6, 7, 'a', 'b', 'c', True, 99]

# remove item from list without pop
l1.remove(3)
print(l1)

# for duplicates, remove method will remove first occurance of that element
my_list = ['apple', 1, True, 1, 'book', 'apple', 1]
my_list.remove('apple')
print(my_list) # [1, True, 1, 'book', 'apple', 1]

# del method
del my_list[3]  
print(my_list) # [1, True, 1, 'apple', 1]

# del my_list # does not exists any more
# print(my_list) # NameError: name 'my_list' is not defined

l1.clear() # clears all list elements
print(l1) # [], empty list

# sort list
new_list = [2,5,-6,-3,6,87,1,0,-2,3,-4]
new_list.sort()
print(new_list) # [-6, -4, -3, -2, 0, 1, 2, 3, 5, 6, 87]

new_list = [2,5,-6,-3,6,87,1,0,-2,3,-4]
new_list.sort(key = abs) # takes any function that func(list_element) -> to_sort
print(new_list) # [0, 1, 2, -2, -3, 3, -4, 5, -6, 6, 87]

thislist = ["banana", "Orange", "Apple", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['Apple', 'banana', 'cherry', 'Orange'] 
 
thislist.reverse()
print(thislist) # ['Orange', 'cherry', 'banana', 'Apple']

###################### List Copy ######################
l1 = [2,5,4,3,6,7,8]
l2 = l1
print(l2)
l1.pop()
print(l2) # we used pop to l1, but item was removed from l2 also

# list can not be copied by assignment, when we do l2 = l1, l2 will 
# only be reference to l1, not a copy 

# copy method, also known as deep copy
l2 = l1.copy()
print('Deep copy will make new list')
print(l2)
l1.pop()
print(l2) # not affected by any operations done on l1

# bad way to deep copy
l2 = list(l1) # this will construct new list with the iterable l1
print(l2)
l1.pop()
print(l2) # also not affected by any operations done on l1

list_with_dups = ['apple', 4, 'b', 4, 'apple', 4]
print(list_with_dups.count('apple'))
print(list_with_dups.count(4))

#################### Overview ####################
# Method	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list




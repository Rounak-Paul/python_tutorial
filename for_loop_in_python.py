# Python has 2 built in loops:
# -> for loop
# -> while loop

# for loop

# syntax:
# for <item> in <iterable>:
#   do something

my_list = [1, 2, 3, 'apple', True, 'book', 4, False]

for item in my_list:
    print(item)

# range(start_included, end_excluded, step)
my_range = range(0, 10, 1)
print(my_range)

for item in my_range:
    print(item)

# break
for item in my_range:
    print(item)
    if item == 5:
        print(f'break called at: {item}')
        break # exit the current loop

# continue
for item in my_range:
    if (item == 5):
        continue # discard current loop iteration and move to next 
    print(item)

# pass
print("start of for loop with pass")
for item in my_range:
    pass # loops can not be empty, pass will act as "Do Nothing" logic
print("end of for loop with pass")

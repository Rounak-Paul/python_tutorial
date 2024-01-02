empty_list = []
not_empty_list = [1,2,3,4,5]

empty_str = []
not_empty_str = "Happy New Year!"

#check if list if empty

# result = (len(empty_list) != 0)
# print(f"list is not empty: {result}")

# result = (len(not_empty_list) != 0)
# print(f"list is not empty: {result}")

# THE BOOL TYPECAST

result = bool(empty_list)
print(f"list is not empty: {result}")

result = bool(not_empty_list)
print(f"list is not empty: {result}")

if (bool(not_empty_list)):
    # Do something
    pass

result = bool(empty_str)
print(f"str is not empty: {result}")

result = bool(not_empty_str)
print(f"str is not empty: {result}")


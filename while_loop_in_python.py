# While loop

# syntax:
# while <condition>:
#   do something

i = 0

while i < 7:
    print(i)
    i += 1

# while loop will keep on running if no break condition is there

i = 0
while True:
    print(i)
    i += 1
    if i == 7:
        break

# EX: pop and clear list

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Pop and clear list")

while len(my_list) > 0:
    item = my_list.pop()
    print(item)

print(my_list)

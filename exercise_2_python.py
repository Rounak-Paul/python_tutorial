''' 
This exercise will draw knowledge from the following concepts: 

- List
- For loop
- Indexing

'''

'''
----- Problem statement -----
Given an integer depth, print the Pascal's triangle .

In Pascal's triangle, each number is the sum of the two 
numbers directly above it.

'''

depth = 10

output=[]
output.append([1])
for i in range(depth-1):
    print(i)
    newRow=[1]
    for j in range(i):
        newRow.append(output[i][j]+output[i][j+1])
    newRow.append(1)
    output.append(newRow)

for row in output:
    row_str = str(row)
    row_str = row_str.center(40, " ")
    print(row_str) 
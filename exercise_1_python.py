''' 
This exercise will draw knowledge from the following concepts: 

- Typecast
- List
- Slicing
- If condition
- For loop
- Indexing
- String

'''

'''
----- Problem statement -----
Given a string s, reverse only all the vowels in the string 
and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can 
appear in both lower and upper cases, more than once.

----- Example 1 -----
Input: s = "hello"
Output: "holle"

----- Example 2 -----
Input: s = "leetcode"
Output: "leotcede"
'''



s = "hello"  # holle

s = list(s) # typecast
print(s)

v = ["a", "e", "i", "o", "u"]

v_index = []
v_val = []

for i in range(len(s)):
    if s[i].lower() in v:
        v_val.append(s[i])
        v_index.append(i)

print(v_index)
print(v_val)

v_val = v_val[::-1]
for i in range(len(v_index)):
    s[v_index[i]] = v_val[i]

output = ''.join(s)

print(output) # raunok
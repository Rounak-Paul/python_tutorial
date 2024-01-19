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



s = "rounak" # raunok

s = list(s)
v = ["a","e","i","o","u"]
val = []
pos = []
for i in range(len(s)):
    if s[i].lower() in v:
        val.append(s[i])
        pos.append(i)
val = val[::-1]
for i in range(len(pos)):
    s[pos[i]] = val[i]
output = ''.join(s)

print(output)
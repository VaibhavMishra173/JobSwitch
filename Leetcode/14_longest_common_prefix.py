# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

import string

strs = ["flower","flow","flight"]

strs = ["dog","racecar","car"]

l_p=[]

strs=sorted(strs)
first=strs[0]
last=strs[-1]

for i in range(len(first)):
    if len(last)>i and last[i]==first[i]:
        l_p.append(last[i])
        print(len(last),i)

l_p=''.join(map(str,l_p))

print(l_p,strs)



# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# a='rat'
# b='car'

# a="anagram"
# b="nagaram"

# a="anagram"
# b="nagaram"

# a='aacc'
# b='ccac'

str1="anagram"
str2="nagaram"

str1=sorted(str1)
str2=sorted(str2)

print(str1)
print(str2)

if str1==str2:
    print ("True")
else:
    print("False")
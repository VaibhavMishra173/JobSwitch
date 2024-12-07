# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


s = "()"
s = "()[]{}"
# s = "(]"
# s=']'
# s='){'
# s='(])'

st=[]

inpt=list(s)
if len(inpt)>1:
    for i in range(len(inpt)):
        if len(st)==0:
            st.append(inpt[i])
        elif inpt[i]=='(' or inpt[i]=='{' or inpt[i]=='[':
            st.append(inpt[i])
        elif inpt[i]==')' and st[len(st)-1]=='(':
            st.pop()
        elif inpt[i]=='}' and st[len(st)-1]=='{':
            st.pop()
        elif inpt[i]==']' and st[len(st)-1]=='[':
            st.pop()
        elif inpt[i]==')' or inpt[i]=='}' or inpt[i]==']':
            st.append(inpt[i])
else:
    st.append(inpt[0])


print(st)

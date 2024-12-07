# s = 'asdasdkfvfdvmssdte'
# s = "tutorialspointfordeveloper"
# s='abcab'
# s='geeksforgeeks'
s='for'
str=s

while len(s)!=0:
    ch=s[0]
    s0=len(s)
    s=s.replace(ch, '')   
    s1=len(s)
    if s1==s0-1:
        break

for i in range(len(str)):
    if ch==str[i]:
        print(ch,i)


# first print all subsequence


s1="abcdef"
s2="ae"

i=0
j=0

m=len(s1)-1
n=len(s2)-1

a=min(m,n)
b=a

while a!=0 and i<m and j<n:
    if s1[i]==s2[j]:
        i+=1
        j+=1
        a-=1
    else:
        i+=1

print(b==j,b,j)

from re import X


def count(n):
    res=0
    while(n>0):
        n=(n&(n-1))
        res+=1
    return res

x = 7

print(count(X))
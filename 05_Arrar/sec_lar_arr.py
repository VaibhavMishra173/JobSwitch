def find(a):
    res = 0
    for i in range(1,len(a)-1):
        if(a[i]>a[res]):
            res=i
            
    return res

def sndlar(a):
    lar = find(a)
    res = -1
    for i in range(0,len(a)-1):
        if (a[i]!=a[lar]):
            if(res==-1):
                res=i
            elif(a[i]>a[res]):
                res=i
    
    return res

a=[111,911,7,112,34,65,45]

print(sndlar(a))
# print(a)
# a.sort()
# print(a)
# print(b)
# print(sorted(a))

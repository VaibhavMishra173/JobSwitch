def find(a):
    res = 0
    for i in range(1,len(a)-1):
        if(a[i]>a[res]):
            res=i
            
    return res

a=[111,911,7,11,34,65,45]

print(find(a))
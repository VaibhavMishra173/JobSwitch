def insert(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a

a=[20,5,40,60,10,30]
print(insert(a))
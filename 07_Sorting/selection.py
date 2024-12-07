def sort(a):
    for i in range(0,len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if(a[j]<a[min_index]):
                min_index=j
        a[min_index],a[i]=a[i],a[min_index]
    return a

a=[10,5,8,20,2,18]
print(sort(a))
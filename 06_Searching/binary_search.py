


def linearsearch(a,b):
    for i in range(len(a)):
        if (a[i]== b):
            return i
            break
    return -1

def binarysearch(a,b):
    low=0
    high=len(a)-1
    while(low<=high):
        mid=int((low+high)/2)
        if (a[mid]==b):
            return mid
        elif(a[mid]>b):
            high=mid-1
        else:
            low=mid+1
    
    return -1

def recursive_bs(a,b,l,h):
    if(l>h):
        return -1
    mid = int((l+h)/2)
    if(a[mid]==b):
        return mid
    elif(a[mid]>b):
        return recursive_bs(a,b,l,mid-1)
    else:
        return recursive_bs(a,b,mid+1,h)
    
    return -1    

a=[2,3,4,5,6,7,8,12,23,34,45,56,67,78,89]
x=7
# x=1
low=0
high=len(a)-1
print(recursive_bs(a,x,low,high))

# print(linearsearch(a,x))
# print(binarysearch(a,x))
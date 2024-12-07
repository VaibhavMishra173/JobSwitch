

from re import I


def search(a,b):
    l=0
    h=len(a)
    while(l<=h):
        mid=int((l+h)/2)
        if(a[mid]==b):
            return mid
        if(a[l]<a[mid]):
            if(b>=a[l] and b<a[mid]):
                h=mid-1
            else:
                l=mid+1
        else:
            if(b>=a[mid] and b<=a[h]):
                l=mid+1
            else:
                l=mid-1
    return -1

a=[10,20,30,40,50,8,9]

print(search(a,30))
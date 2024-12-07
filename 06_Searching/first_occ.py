
# first occurence of a no. in an sorted array


def first(a,b):
    l=0
    h=(len(a)-1)
    while(l<=h):
        mid = int((l+h)/2)
        if(a[mid]>b):
            h=mid-1
        elif(a[mid]<b):
            l=mid+1
        else:
            if(mid==0 or a[mid]!=a[mid-1]):
                return mid
            else:
                h=mid-1
    

# a=[5,10,10,20,20]
a=[10,20,20,20,30,30]

b= 20

print(first(a,b))
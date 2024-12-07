

# def cnt(a,b):
#     cnt=0
#     for i in range(len(a)):
#         if a[i]==b:
#             cnt+=1
        
#     return cnt


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
                
def last(a,b):
    l=0
    h=(len(a)-1)
    while(l<=h):
        mid = int((l+h)/2)
        if(a[mid]==b):
            if(mid==(len(a)-1) or a[mid]!=a[mid+1]):
                return mid
            else:
                l=mid+1
            # return mid
        elif(a[mid]>b):
            h=mid-1
        elif(a[mid]<b):
            l=mid+1

def cnt(a,b):
    f=first(a,b)
    l=last(a,b)
    if f==-1:
        return -1
    else:
        # return l,f,l-f+1
        return l-f+1


a=[10,20,20,20,30,30]

b= 10

print(cnt(a,b))
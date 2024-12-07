
# last occurence of a no. in an sorted array


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
        # else:
        #     if(mid==(len(a)-1) or a[mid]!=a[mid+1]):
        #         return mid
        #     else:
        #         l=mid+1
        
    return -1
    

a=[5,10,10,20,20,30,40,40,40]

'''

Round 1
a[0]=5
a[len(a)-1]=20   --> a[4]

a[mid]=10    --> a[2]

a[mid]==b  False

a[mid]>b   --> b= 20     10 > 20 false


a[mid]<b   --> b= 20     10 < 20 true
    l=mid+1   --> l=2+1 l=3
    
ROund 2

mid = (3+4)/2   --> 3

a[mid]==b   --> True

    

    







'''




# b= 20
b=40
# b=400

print(last(a,b))
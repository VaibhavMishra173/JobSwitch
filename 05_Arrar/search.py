from re import I


def search(a,b):
    for i in range(0,len(a)):
        if(a[i]==b):
            return i
    return -1

a=[20,2,9,11,5,7,25]

# a=input()
# b=input("Enter the element to find :")
b=5
print(search(a,b))
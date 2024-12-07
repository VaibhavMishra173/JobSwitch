# print double sided stair case in python

# def pattern(n):
#     for i in range(1,n+1):
#         s="#"*i
#         print(s.rjust(n))

def pattern(n):
    for i in range(1,n+1):
        if(i%2 !=0):
            k=i+1 
        for g in range(k,n):
            if (g>=k):
                print(end=" ")
        for j in range(0,k):
            if(j==k-1):
                print("*")
            else:
                print("*",end=" ")

# row=int(input("Enter number of rows: "))
row=12

pattern(row)
# print(end=" ")
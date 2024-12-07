# sum of first n natural number 

############## My Program ########### Average time #######

# def sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#     return sum

# n = int(input("Enter the number : "))
# print(sum(n))


############ least time or constant time ####### 

def sum(n):
    return n*((n+1)/2)

num = int(input("Enter the number to find the sum : "))

print(sum(num))


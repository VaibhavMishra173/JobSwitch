

# def check(n):
#     bool = True
#     for i in range (2,int(n/2)):
#         if (n%i==0):
#             bool = False
        
#     return bool

# a = int(input("Enter first number : "))

# print(check(a))


# Efficient method 




from cmath import sqrt


def check(n):
    a = sqrt(n)
    for i in range(2,int(a.real)):
        if (n%i == 0):
            return False        
    return True


a = int(input("Enter first number : "))

print(check(a))
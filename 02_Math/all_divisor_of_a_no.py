

# def check_divisor(n):
#     for i in range(1,n+1):
#         if (n%i==0):
#             print(i)

# a = int(input("Enter first number : "))

# check_divisor(a)




# from cmath import sqrt


# def check_divisor(n):
#     for i in range(1,int(sqrt(n).real)+1):
#         if (n%i==0):
#             print(i)
#             if(i!=n/i):
#                 print(n/i)

# a = int(input("Enter first number : "))

# check_divisor(a)


from cmath import sqrt


def check_divisor(n):
    i = 1
    for i in range(1,int(sqrt(n).real)):
        if (n%i==0):
            print(i)
    for i in range(i,1):
        if(n%i==0):
            print(n/i)

a = int(input("Enter first number : "))

check_divisor(a)
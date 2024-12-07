# from cmath import sqrt

# def check_factor(n):
#     if (n<=1):
#         return n
#     for i in range(2,int(sqrt(n).real)):
#         while(n%i==0):
#             print(i)
#             n=n/i
#     if(n>1):
#         print(n)

# a = int(input("Enter first number : "))

# check_factor(a)



from cmath import sqrt

def check_factor(n):
    if (n<=1):
        return n
    while(n%2==0):
        print(2)
        n=n/2
    while(n%3==0):
        print(3)
        n=n/3
    for i in range(5,int(sqrt(n).real),6):
        while(n%i==0):
            print(i)
            n=n/i
        while(n%(i+2)==0):
            print(i+2)
            n=n/(i+2)
    if(n>3):
        print(n)

a = int(input("Enter first number : "))

check_factor(a)
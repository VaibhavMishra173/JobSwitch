
# naive method 

# def gcd(a,b):
#     result = min(a,b)
#     while(result>0):
#         if(a%result == 0 and b%result == 0):
#             break
#         result -= 1
#     return result

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# print(gcd(a,b))



# efficient method


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print(gcd(a,b))
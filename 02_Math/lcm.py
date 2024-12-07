
# Naive method 


# from unittest import result


# def lcm(a,b):
#     result = max(a,b)
#     while(1):
#         if(result%a==0 and result%b==0):
#             return result
#         result += 1
#     return result

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# print(lcm(a,b)) 


# Efficient method 

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b)/gcd(a,b)


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print(lcm(a,b))



def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

a=5000000
b=8000
num=(gcd(a,b))
ratio=5000000/num
ratio1=8000/num
print(int(ratio1),":",int(ratio))
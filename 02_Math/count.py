from cmath import log, log10

def count(n):
    cnt = log10(n)+1
    return int(cnt.real)

num=int(input("Enter number : "))

print(count(num))

# when i am taking log10 of any number it return its value in complex number
# so as we need only floor of real part of complex number  
# so i am taking only real part converting it into integer to femove the decimal value of real part 


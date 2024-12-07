# Find Square of a number without using multiplication and division operator

def sum(a):
    sum=0
    for i in range(a):
        sum+=a
    return sum


a=5

# mine 
b=pow(a,2)
print(b)

# Given
print(sum(a))
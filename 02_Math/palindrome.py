

from audioop import reverse
from math import remainder
import numbers
from pickle import FALSE, TRUE
from turtle import right


def palindrome(n):
    rev = 0
    temp = n
    while(n > 0):
        remainder = n % 10
        rev = (rev * 10) + remainder
        n = n // 10
    if (temp == rev):
        return print("TRUE")
    else:
        return print("FALSE")
    

num = int(input("Enter number : "))

if(num>0):
    palindrome(num)

else :
    print ("Enter number greater than 0 !")
    


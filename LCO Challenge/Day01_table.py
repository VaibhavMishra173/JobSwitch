# there was a teacher in small town who loves coding and he wants to create a program which print out the whole multiplication table of an entered number for his students .
#  in python 


from re import I


def tab(a):
    for i in range(1,11):
        print(a,"X",i,"=",a*i )

num = int(input("Enter the number: "))

tab(num)
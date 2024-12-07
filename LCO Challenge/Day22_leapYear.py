
year=int(input("Enter Year:"))

flag=False

if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            flag=True
        else:
            flag=False
    else:
        flag=True
else:
    flag=False

if flag:
    print("The year is a leap year (it has 366 days)")
else:
    print("The year is not a leap year (it has 365 days).")
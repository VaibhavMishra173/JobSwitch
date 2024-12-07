# Program to calculate an angle between hour hand and minute hand .
# check whether the minute hand overlap hour hand at a given time

# Mine

# number_of_hours=int(input("enter hours: "))
# number_of_minutes=int(input("enter minutes: "))


# Anglehrs = float(30 * number_of_hours) + float(0.5 * number_of_minutes)
# Anglemins = float(6 * number_of_minutes)
# angle=float(Anglehrs - Anglemins)
# print(f"the angle between {number_of_hours}:{number_of_minutes} is {angle}O")
# if angle==0:
#     print("they overlaps")


# Provided

def calcAngle(h,m):
    if(h<0 or m<0 or h>12 or m>60):
        print("Wrong Input")
    if h==12:
        h=0
    if m==60:
        m=0
    hour_angle=0.5*(h*60+m)
    minute_angle=6*m
    angle=abs(hour_angle-minute_angle)
    angle=min(360-angle,angle)
    return int(angle)

h=int(input("Enter hour(1-12): "))
m=int(input("Enter minute(0-59): "))
clockAngle=calcAngle(h,m)
if clockAngle==0:
    print("hour and minute hands overlaps")
else:
    print(clockAngle,"degree")

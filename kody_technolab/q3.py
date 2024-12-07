
step=int(input("enter the no. of steps"))

uper=0
dnwrd=0
lft=0
rght=0

for i in range(step):
    s=input(f"enter step {i+1}")
    if s=='up':
        if dnwrd==0:
            uper+=5
        else:
            uper-=5
    if s=='down':
        if uper==0:
            dnwrd+=3
        else:
            uper-=3
    if s=='left':
        if rght==0:
            lft+=3
        else:
            rght-=3
    if s=='right':
        if lft==0:
            rght+=2
        else:
            lft-=2

print(f'coordinate of robot in upper direction in {uper},dwon direction is {dnwrd},left dicrection is {lft},right direction is {rght}')
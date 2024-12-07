a=[1,2,3,4,5]
b=[2,3,4,7,9,11,15]

c=a+b

for i in range(len(c)-1):
    for j in range(len(c)-1-i):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]

print(c)

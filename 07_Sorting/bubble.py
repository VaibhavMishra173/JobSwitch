
def bub(a):
    for  i in range(0,len(a)-1):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            
    return a

def bub_eff(a):
    for  i in range(0,len(a)-1):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            
    return a



a=[2,10,8,7]
# print(bub(a))
print(bub_eff(a))

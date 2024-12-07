
# def lead(a):
#     curr=a[len(a)-1]
#     print(curr)
#     n=len(a)-2
#     for i in range(n,0,-1):
#         if(curr<a[i]):
#             curr=a[i]
#             print(curr)
    

# a=[2,10,4,3,6,5,2]

# lead(a)

    
    
from tkinter import PIESLICE


def leader(a):
    lead=[]
    for i in range(1,len(a)-2):
        if(a[0]>a[1]):
            lead.append(a[0])
        if(a[i]>a[i+1] and a[i]>a[i-1]):
            lead.append(a[i])   
    if(a[len(a)-1]>a[len(a)-2]):
        lead.append(a[len(a)-1])
    print(lead)


a=[2,10,4,3,6,5,2,7]
# print(a)
leader(a)
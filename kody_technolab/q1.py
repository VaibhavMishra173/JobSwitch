# Q1. program to print words from a sentence with highest and lowest no. of vovel characters

def hig(a):
    v=['a','e','i','o','u']
    cntr=[]
    for i in a:
        cnt=0
        b=list(i)
        for j in v:
            for k in b:
                if k==j:
                    cnt+=1
        # mi=0
        # mi1=cnt
        # minimum=min(mi,mi1)
        # mx=cnt
        # mx1=0
        # maximum=max(mx,mx1)
        cntr.append(min)
    cntr.sort()
    print(cntr)
    # print(f"highest count is {cntr[len(cntr)-1]} and lowest is {cntr[0]}")

a= "program to"
# print words from a sentence with highest and lowest no. of vovel characters"
# a=input()
arr=list(a.split(" "))
hig(arr)

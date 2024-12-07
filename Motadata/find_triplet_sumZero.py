
def triplet(a):
    for i in range(0,len(a)-2):
        for j in range(i+1,len(a)-1):
            for k in range(j+1,len(a)):
                # print(i,j,k)
                if (a[i]+a[j]+a[k]==0):
                    print(f'''sum found at index {i},{j},{k} and value is {a[i]}{a[j]}{a[k]}''')

arr=list(map(int,input().split(",")))
# arr=[0, -1, 2, -3, 1]
triplet(arr)
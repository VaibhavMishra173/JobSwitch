# a=input()
# arr=list(a.split(" "))
arr=[54,4,3,6,7]
dig=input()
dig=str(7)
cnt=0

for i in arr:
    numb=str(i)
    print(numb,type(numb))
    if dig in numb:
        cnt+=1
        print(cnt)

# print(arr)
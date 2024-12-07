# a=input()
# arr=list(a.split(" "))
arr=[5,4,3,6,7]
# dig=input()
dig=7

for i in range(len(arr)):
    if arr[i] == dig:
        arr.pop(i)

print(arr)
# given a sorted array and find the first and last position of target and if not found return [-1,-1]

def find_index(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            start=i
            while i+1 < len(arr) and arr[i+1] == target:
                i+=1
            return [start,i]
    return[-1,-1]

arr=[2,4,5,5,5,5,5,7,9,9]
arr=[2,4,7,5,9,9]
target=5
print(find_index(arr,target))

#  this will store data of previous array in new and remove zero from the 
# new array and return count
# def cnt1(a,b):
#     rem=0
#     na=a
#     for i in range(len(a)):
#         if rem in na:
#             na.pop(rem)
#     return len(na)



# this will check the first occurence of 1 and we will subtract it from the len of array 
def cnt1(a,b):
    for i in range(len(a)):
        if a[i]==1:
            return len(a)-i
            break

a=[0,0,0,1,1,1,1,1]

b=1
print(cnt1(a,b))
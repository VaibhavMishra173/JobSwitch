# Product of Array Except Self

# Solution
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
nums = [0,0]
nums = [2,3,0,0]
nums = [-1,1,0,-3,3]
nums = [-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
prdt_array=[]


for i in range(len(nums)):
    prdt = 1
    for j in range(len(nums)):
        if i==j:
            continue
        else:
            # print(prdt,j)
            prdt*=nums[j]
    prdt_array.append(prdt)

            
print(prdt_array)

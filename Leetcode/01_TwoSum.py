# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]



from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    #     for i in range(0,len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if (nums[i]+nums[j]==target):
    #                 return i,j

        comp_map={}
        for i,n in enumerate(nums):
            comp=target-n
            if comp not in comp_map:
                comp_map[n]=i
            else:
                return [i,comp_map[comp]]
            
# my own logic need to check 

# a=[4,5,6,7,8,8]
# for i in a:
#     if(a[i]+a[i+1]==16):
#         print(i,i+1)
#     if i == len(a)-2:
#         break
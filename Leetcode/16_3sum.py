# 16. 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
 

# Constraints:

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


nums = [0,0,0]

# nums = [-1,2,1,-4]
target = 1
# nums=[1,1,1,0]
# target=-100

summ1=10000000000
if len(nums)>=4:
    for i in range(0,len(nums)-3):
        summ = nums[i]+nums[i+1]+nums[i+2]
        # print(summ)
        summ1=min(summ1,summ)
        # print(summ1)
else:
    if len(nums)>3:
        summ = nums[0]+nums[1]+nums[2]
        summ1=min(summ1,summ)
        summ2= nums[1]+nums[2]+nums[3]
        summ1=min(summ1,summ2)
    else:
        summ = nums[0]+nums[1]+nums[2]
        summ1=min(summ1,summ)

print(summ1)

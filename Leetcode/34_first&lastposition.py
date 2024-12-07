# 34. Find First and Last Position of Element in Sorted Array
# Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

nums = [5,7,7,8,8,10,12]
target = 8

for i in range(len(nums)):
        if nums[i]==target:
            start=i
            while i+1 < len(nums) and nums[i+1] == target:
                i+=1
            return [start,i]
    return[-1,-1]





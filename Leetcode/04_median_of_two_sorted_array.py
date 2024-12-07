# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106



nums1 = [1,2]
nums2 = [3,4]

nums=nums1+nums2
nums.sort()
print(nums)
m=len(nums1)
n=len(nums2)
lenth=m+n
print(lenth,m,n)
if lenth%2!=0:
    med=float(nums[int(lenth/2)])
    print(int(lenth/2)+1)
else:
    fst=nums[int(lenth/2)-1]
    snd=nums[int(lenth/2)]
    print(fst,snd)
    med=float((fst+snd)/2)

med=format(med,".5f")
print(float(med))
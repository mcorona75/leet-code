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

# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

 

# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Combine the lists
        nums = nums1+nums2

        #Sort the lists
        nums = sorted(nums)

        #Get length of the final list once
        length = len(nums)

        #if the length is even basically
        if (length/2).is_integer():
            #Return the average of the two middle index by offsetting the length
            return (nums[int((length+1)/2)]+nums[int((length-1)/2)])/2
        else:
            #Return the middle index! Luckily the typecast to int by default is a floor function
            #IE if the length is 3, you want to return index 1 (0th,1st,2nd). 3/2 = 1.5 the int typecast will return 1
            #int(1.99) will return 1
            return nums[int((length/2))]

sol = Solution
print(sol.findMedianSortedArrays(sol,[1,2],[3]))

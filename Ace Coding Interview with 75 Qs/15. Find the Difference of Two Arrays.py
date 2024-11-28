import numpy as np
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1, set2 = set(nums1), set(nums2)

        results1 = list(set1 - set2)
        results2 = list(set2 - set1)

        return [results1, results2]
    
# test solution 

solution = Solution()
nums1 = [1,2,3]
nums2 = [2, 2, 2, 4, 6]
print(solution.findDifference(nums1, nums2))  # Output: [[], [5]]



 
import pandas as pd 

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        freq = {}
        for num in nums :
            complement = k - num
            if complement in freq and freq[complement] > 0:
                count += 1
                freq[complement] -= 1

            else :
                if num in freq :
                    freq[num] += 1
                else :
                    freq[num] = 1
        return count 
# Test solution
nums = [1, 2, 4, 2, 3]
k = 5
solution = Solution()
print(solution.maxOperations(nums, k))  # Output: 2


# Test solution
nums = [1, 2, 4, 2, 3]
k = 5
solution = Solution()
print(solution.maxOperations(nums, k))  # Output: 2

# test solution 

nums = [1,2,4,2,3]
k = 5
solution = Solution()
print(solution.maxOperations(nums, k))  # Output: 2


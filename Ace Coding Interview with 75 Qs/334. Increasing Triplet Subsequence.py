import pandas as pd 
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        n = len(nums)
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return print('first :', first, '\nsecond:', second)
# Test the function 
solution = Solution()
print(solution.increasingTriplet([0, 1, -1, 2])) 



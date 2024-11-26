import pandas as pd 
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0 :
                nums[write] = nums[read]
                write += 1

        for w in range (write, len(nums)):
            nums[w] = 0

        return nums 
    


# test solution
nums = [0,1,0,3,12]
# nums = [0]
# nums = [0,0,1]
solution = Solution()
output = solution.moveZeroes(nums)
print(output)
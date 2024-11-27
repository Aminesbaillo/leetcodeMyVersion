 
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot_index=  -1
        sum_left, sum_right = 0, sum(nums)

        for i in range(len(nums)):
            sum_right -= nums[i]
            if i != 0 : 
                sum_left += nums[i-1]
                
            if sum_left == sum_right :
                pivot_index = i 
        return pivot_index
    
# test the solution

solution = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(solution.pivotIndex(nums))
            
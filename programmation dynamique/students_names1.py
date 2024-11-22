class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the sum of nums[i] and nums[j] equals the target
                if nums[i] + nums[j] == target:
                    # If so, return the indices i and j as a list
                    list_result = [i, j]
                    return list_result 
                    break 
nums = [2,7,11,15]
target =  9             
solution = Solution()
print(solution.twoSum(nums, target))
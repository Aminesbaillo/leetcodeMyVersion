class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        results = [1] * n
        prefix = 1
        for i in range(n):
            results[i] = prefix 
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            results[i] *= suffix 
            suffix *= nums[i] 

        return results       
            
# Testing the class with a sample input

nums = [1,2,3,4]
solution = Solution()
output = solution.productExceptSelf(nums)
print(output)  # Output: [24, 12, 8, 6]


# nums_2 = [-1,1,0,-3,3]
# solution_2 = Solution()
# output_2 = solution_2.productExceptSelf(nums_2)
# print(output_2)  # Output: [0,0,9,0,0]
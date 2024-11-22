class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0 
        for num in nums : 
            binary_representation = bin(nums.index(num))[2:]
            if binary_representation.count('1') == k :
                result += num 
        return result
solution = Solution()
nums= [5,10,1,5,2]
k = 1
print(solution.sumIndicesWithKSetBits(nums, k))


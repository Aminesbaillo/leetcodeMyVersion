class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        threshold = max(candies)
        results = [cand + extraCandies >= threshold for cand in candies]
        return results 

# Test the function with given examples

solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))

print(solution.kidsWithCandies([4,2,1,1,2], 1))

print(solution.kidsWithCandies([12,1,12], 10))
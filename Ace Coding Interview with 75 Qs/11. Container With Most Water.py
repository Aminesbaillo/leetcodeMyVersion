class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        left = 0
        right = len(height) - 1
        results = 0
        while left < right:
            water_volume = min(height[left], height[right]) * (right - left)
            if results < water_volume:
                results = water_volume
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return results
    
# test the solution

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
output = solution.maxArea(height)
output
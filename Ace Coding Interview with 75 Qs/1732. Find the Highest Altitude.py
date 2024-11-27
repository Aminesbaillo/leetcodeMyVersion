 
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_gain, current_gain = 0, 0
        for elm in gain :
            current_gain += elm
            if current_gain > max_gain :
                max_gain = current_gain
        return max_gain
    
# Test the solution

solution = Solution()
gain = [-5,1,5,0,-7]
print(solution.largestAltitude(gain))  # Output: 1
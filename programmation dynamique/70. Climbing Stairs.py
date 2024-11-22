import math 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1 
        two = 1
         
        for i in range (0, n-1):
            temp = two
            two = two + one
            one = two
        return two
    
solutions = Solution()
res = solutions.climbStairs(4)
print(res)
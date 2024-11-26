import pandas as pd 
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        t_len =  len(t)
        if s_len > t_len: 
            return False 
        elif s_len == 0:
            return True  # if s is empty, t is also a subsequence of s
        else :
            write  = 0 
            for read in range(t_len):
                if t[read] == s[write] :
                    write += 1 
                if write == s_len :  
                    return True
            return False
        
# test the solution

s = "abc"
t = "ahbgdc"
solution = Solution()
output = solution.isSubsequence(s, t)
output

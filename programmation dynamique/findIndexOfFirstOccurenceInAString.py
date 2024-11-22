class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
    
        m = len(needle)
        n = len(haystack)
        i = 0
        while  i < n :
            if haystack[i:i+m] == needle :
                return i 
            else :
                i += 1
        return -1
    
solution = Solution()
print(solution.strStr("sasdbutsad","sad"))
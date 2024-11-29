class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        stack = []
        while i < len(s) :
            if s[i] == '*' :
                stack.pop()
            else :
                stack.append(s[i])
            i += 1
           
          

        return ''.join(stack)
    
# Test the function

s = "leet**cod*e"
solution = Solution()
print(solution.removeStars(s)) # Output: "leetcodeisamazing"
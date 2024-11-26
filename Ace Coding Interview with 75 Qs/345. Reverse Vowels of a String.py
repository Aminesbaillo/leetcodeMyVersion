import pandas as pd 
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
         
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        u = 0
        for i in range(len(s)):
            if s[i].lower() in vowels:
                j = len(s) - 1 - u
                while j > i:
                    if s[j].lower() in vowels:
                        d = s[i]
                        s[i] = s[j]
                        s[j] = d
                        u = len(s) - j 
                        break
                    j -= 1
        return "".join(s)    
# Testing the class with a sample input

s = 'IceCreAm'
solution = Solution()
reversed_s = solution.reverseVowels(s)
print(reversed_s) 



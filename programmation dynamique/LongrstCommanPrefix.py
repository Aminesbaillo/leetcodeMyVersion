class Solution(object):
       def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        i = 0
        n = len(strs)
        loop = True
        count = 0
        if n == 0:
            return ""
        min_len = min(len(item) for item in strs)
        listOfResult = []
        for i in range(min_len):
            l=[]
            for j in range(n):
                l.append(strs[j][i])
                l = list(set(l))
            if len(l) == 1 :
               listOfResult.append(l[0]) 
            else :
                  break     
        return "".join(listOfResult)
solution = Solution()
print(solution.longestCommonPrefix([""])) 

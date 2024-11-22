class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        S = list(s)
        stack = []
        for i in range(n):
            if S[i] == '(':
                stack.append(i)
            elif S[i] == ')':
                if stack:
                    stack.pop()
                else: 
                    S[i] = ""
        for j in stack:
            S[j] = ""
        return "".join(S)


solution = Solution()
print(solution.minRemoveToMakeValid("lee(t(c)o)de)("))




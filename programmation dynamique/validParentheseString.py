class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        S = list(s)
        open = []
        stack = []
        for i in range(n):
            if S[i] == '(' :
                open.append(i)
            elif S[i] == '*': 
                stack.append(i)
            else:
                if open:
                    open.pop()
                elif stack:
                    stack.pop()
                else :
                    return False
        i = 0 
        while open:
            if stack:
                if open[i] < stack[i]:
                    open, stack = open[i+1:], stack[i+1:]
                    i -= 1
                elif open[i] > stack[i]:
                    stack = stack[i+1:]
                    i -= 1
            else :
                return False
            i += 1
        return True
solution = Solution()
# print(solution.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(solution.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
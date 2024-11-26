# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         """
#         :type str1: str
#         :type str2: str
#         :rtype: str
#         """
#         len1, len2 = len(str1), len(str2)
#         min_len = min(len1, len2)
#         divisors = []
#         for i in range(1, min_len + 1):
#             if len1 % i == 0 and len2 % i == 0 :
#                 divisors.append(i)
#         for d in reversed(divisors):
#             condidate = str1[:d]
#             # check if condidate can form both strings : 
#             if self.isDivisor(str1, condidate) and self.isDivisor(str2, condidate):
#                 return condidate
#         return ""
#     def isDivisor(self, str1, condidate):
#         repeat_count = len(str1) // len(condidate)
#         return repeat_count * condidate == str1 

            
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        min_len = min(len1, len2)
        divisors = []


        for i in range(1, min_len+1):
            if len1 % i == 0 and len2 % i == 0 :
                    divisors.append(i)

        for d in reversed(divisors) :
            condidate = str1[:d]
            repeat_count_1 = len(str1)//len(condidate)
            repeat_count_2 = len(str2)//len(condidate)
            if repeat_count_1 * condidate == str1 and repeat_count_2 * condidate == str2:
                return condidate
        return ""        





# Test the solution

solution = Solution()
print(solution.gcdOfStrings('ABCABC', 'ABC'))
# print(solution.gcdOfStrings('ABABAB', 'ABAB'))
# print(solution.gcdOfStrings('LEET', 'CODE'))


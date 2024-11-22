class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r1 = int("".join(map(str, digits)))
        new_digits = r1 + 1
        results = [int(digit) for digit in str(new_digits)]
        return results
soulution_instance = Solution()
res = soulution_instance.plusOne([9,9])
print(res)
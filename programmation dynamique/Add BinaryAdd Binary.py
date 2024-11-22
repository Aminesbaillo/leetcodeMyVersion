class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        results = ""
        carry = 0
        a, b = a[:: -1], b[ :: -1]
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            s = digit_a + digit_b + carry
            results = str(s % 2) + results
            carry = s//2
        if carry:
            results = str(carry) + results
        return results
    
solutions_instance = Solution()
res = solutions_instance.addBinary("11", "1")
print(res)
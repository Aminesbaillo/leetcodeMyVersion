class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        current_vowels = 0
        for i in range(0, k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels
        for i in range(k, len(s)):
            if s[i] in vowels :
                current_vowels += 1
            if s[i-k] in vowels :
                current_vowels -= 1
            if current_vowels > max_vowels:
                max_vowels = current_vowels
            if max_vowels == k :
                return max_vowels

        return max_vowels

# Test the solution

solution = Solution()
s = "abciiidefx"
k = 3
print(solution.maxVowels(s, k))  # Output: 3
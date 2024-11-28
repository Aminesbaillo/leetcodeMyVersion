from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if the lengths are equal
        if len(word1) != len(word2):
            return False
        
        # Step 2: Check if both strings have the same set of characters
        if set(word1) != set(word2):
            return False
        print( sorted(Counter(word1).values()))
        print(sorted(Counter(word2).values()))
        # Step 3: Check if the frequency of characters are the same
        # Compare the frequency counts (sorted to handle different character orders)
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())



solution = Solution()

print(solution.closeStrings("abc", 'bca'))  # Output: True


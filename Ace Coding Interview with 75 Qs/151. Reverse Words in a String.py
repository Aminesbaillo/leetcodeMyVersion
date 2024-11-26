 
import pandas as pd 
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Trim leading and trailing spaces manually
        start, end = 0, len(s) - 1
        while start <= end and s[start] == ' ':
            start += 1
        while end >= start and s[end] == ' ':
            end -= 1
        
        # Step 2: Collect words while removing extra spaces in between
        words = []
        current_word = []
        
        for i in range(start, end + 1):
            if s[i] == ' ':  # Space encountered
                if current_word:  # Push the word if it's non-empty
                    words.append(''.join(current_word))
                    current_word = []
            else:
                current_word.append(s[i])  # Build the current word
        
        # Add the last word if there's any
        if current_word:
            words.append(''.join(current_word))
        
        # Step 3: Reverse the words and join them with a single space
        reversed_words = words[::-1]
        return ' '.join(reversed_words)


# Testing the class with a sample input

s = '  hello    world!  '
solution = Solution()
reversed_s = solution.reverseWords(s)
print(reversed_s)  # Output: 'world! hello'


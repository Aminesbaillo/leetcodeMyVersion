class Solution(object):
    def isPalindrome(self, x):
        """
        Determine if a given integer is a palindrome.

        :type x: int
            The integer to check for palindrome.
        :rtype: bool
            Returns True if the integer is a palindrome, otherwise False.
        """
        # Convert the integer to a string
        str_x = str(x)
        
        # Get the length of the string
        n = len(str_x)
        
        # Initialize a variable to track the position from the start of the string
        i = 0
        
        # Iterate through the first half of the string
        while i < (n // 2):
            # Check if the character at position i matches the character at position -i-1 (from the end of the string)
            if str_x[i] == str_x[-i - 1]:
                i += 1  # Move to the next character
                continue  # Continue to the next iteration of the loop
            else:
                return False  # If the characters don't match, the integer is not a palindrome
        
        return True  # If all characters match, the integer is a palindrome


# Create an instance of the Solution class
solution = Solution()

# Test the isPalindrome method with an example integer
print(solution.isPalindrome(12221))  # Output: True

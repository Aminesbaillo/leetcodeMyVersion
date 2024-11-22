# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

 
# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.





class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize an empty stack to store opening brackets
        stack = []
        
        # A mapping of closing to opening brackets for easy lookup
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Iterate through each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in bracket_map:
                # Check if the current stack is not empty and the top of the stack is the matching opening bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()  # Pop the opening bracket off the stack
                else:
                    # If the stack is empty or the brackets do not match, the string is not valid
                    return False
            # If the character is not a bracket, ignore it (assuming the string only contains brackets)

        # If the stack is empty, all brackets were properly closed; otherwise, the string is not valid
        return not stack

# Create an instance of the Solution class
solution = Solution()

# Test the isValid method and print the result
print(solution.isValid("()[]{}"))  # Expected output: True


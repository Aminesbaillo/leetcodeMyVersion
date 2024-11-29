class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ''
        current_number  = 0

        for char in s: 
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '[' :
                stack.append((current_string, current_number))
                current_string = ''
                current_number = 0
            elif char.isalpha():
                current_string += char
            elif char == ']':
                prev_string, prev_number = stack.pop()
                current_string = prev_string + prev_number * current_string

        return current_string

# Testing the function

s = "3[a]2[bc]"
solution = Solution()
print(solution.decodeString(s))  # Output: 'accaccacc'

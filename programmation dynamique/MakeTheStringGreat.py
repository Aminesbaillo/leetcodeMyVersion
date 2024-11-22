# Make The String Great

# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.



import time 

# Class definition
class Solution(object):
    # Method to remove adjacent characters of opposite cases
    def makeGood(self, s):
        # Record the start time
        start_time = time.time()

        # Initialize an empty stack to store characters
        stack = []

        # Iterate through each character in the input string
        for char in s:
            # Check if the stack is not empty and the current character forms an opposite case pair with the top character of the stack
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                # If so, remove the top character from the stack
                stack.pop()
            else:
                # Otherwise, append the current character to the stack
                stack.append(char)
        
        # Record the end time
        end_time = time.time()

        # Calculate the runtime
        runtime = end_time - start_time

        # Print the runtime
        print("Runtime:", runtime, "seconds")

        # Return the remaining characters in the stack as a string
        return ''.join(stack)


solution = Solution()
print(solution.makeGood("dabBAcCD"))


                    
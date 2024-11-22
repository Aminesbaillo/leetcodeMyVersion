



class Solution(object):
    
    def maxDepth(s):
    max_depth = 0
    current_depth = 0
    
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    
    return max_depth

# # Example usage:
# s1 = "(1+(2*3)+((8)/4))+1"
# print(maxDepth(s1))  # Output: 3

# s2 = "(1)+((2))+(((3)))"
# print(maxDepth(s2))  # Output: 3


solution = Solution()
print(solution.maxDepth((1+(2*3)+((8)/4))+1)) # Output:
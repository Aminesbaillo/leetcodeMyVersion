h# "1004. Max Consecutive Ones III.py" 

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        right, left = 0, 0
        zero_count, max_length = 0, 0

        while right < len(nums):
            # Expand the window by moving the right pointer
            if nums[right] == 0:
                zero_count += 1
            
            # If we have more than k zeros in the window, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the window size and update max_length
            window_size = right - left + 1
            if window_size > max_length:
                max_length = window_size

            # Move the right pointer forward
            right += 1
        
        return max_length

    
# test solution

solution = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 0
print(solution.longestOnes(nums, k))  # Output: 6

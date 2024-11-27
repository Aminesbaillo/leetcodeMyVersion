import time

# Start the timer
start_time = time.time()

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)

        return (max_sum / k) * 1.0

# test the solution

solution = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(solution.findMaxAverage(nums, k))  # Output: 12.75    

# End the timer
end_time = time.time()

# Calculate the time taken
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")
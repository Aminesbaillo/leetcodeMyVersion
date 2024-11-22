class Solution(object):
    def countSubarrays(self, nums, k):
        """
        Count subarrays where the maximum element of nums appears at least k times in that subarray.
        
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Initialize count to store the total count of subarrays
        count = 0
        # Find the maximum element in nums
        max_element = max(nums)
        # Initialize the starting index of the window
        window_start = 0
        # Initialize the count of occurrences of max_element within the current window
        max_count = 0
        
        # Iterate through each element of nums
        for window_end in range(len(nums)):
            # If the current element is equal to max_element, increment max_count
            if nums[window_end] == max_element:
                max_count += 1
            # Debugging: Print current element, window end index, and max_count
            print(f"Element {window_end}: {nums[window_end]}")
            print("Window end:", window_end)
            print("Max count:", max_count)
            print("\n \n")  # Newline for better readability
            
            # If max_count is greater than or equal to k, enter the loop
            while max_count >= k:
                # Increment count by the number of subarrays ending at window_end
                count += len(nums) - window_end
                # If the element at window_start is equal to max_element, decrement max_count
                print('window_start:',window_start)
                if nums[window_start] == max_element:
                    max_count -= 1
                # Move the window forward by incrementing window_start
                window_start += 1
                # Debugging: Print window start index and count after updating
                print("Window start:", window_start)
                print("Count:", count)

        # Return the total count of subarrays
        return count

# Testing the function : 
Solution = Solution()
nums = [1, 5, 4, 4, 4, 5, 2, 3]
k = 2
print(Solution.countSubarrays(nums, k))

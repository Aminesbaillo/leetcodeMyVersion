class Solution:
    def longestSubarray(self, nums):
        left, right = 0, 0
        count_zeros, max_length = 0, 0

        for right in range(len(nums)):
            if nums[right] == 0 :
                count_zeros += 1

            while count_zeros > 1:
                
                if nums[left] == 0 :
                    count_zeros -= 1
                left += 1
            count = right - left + 1
            if max_length < count : 
                max_length = count
        return max_length - 1

    
# test solution
def test_all_cases():
    solution = Solution()

    test_cases = [
        ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5, "After deleting the number in position 4, longest subarray is [1,1,1,1,1]"),
        ([1, 1, 1], 2, "Array of all 1's, delete one to get [1,1]"),
        ([1], 0, "Only one element, delete it (empty array)"),
        ([0], 0, "Only one element, delete it (empty array)"),
        ([0, 0, 0, 0], 0, "Array of all 0's, delete one to get [0]"),
        ([1, 0, 1, 0, 1], 2, "Alternating 1's and 0's, delete one `0` to get [1,1]"),
        ([1, 0, 0, 1, 1, 1], 3, "Deleting one `0` gives [1,1,1,1]"),
        ([0, 1, 1, 1, 1], 4, "Delete `0` at the start to get [1,1,1,1]"),
        ([1, 1, 1, 1, 0], 4, "Delete `0` at the end to get [1,1,1,1]"),
        ([1, 0, 1], 2, "Delete `0` to get [1,1]"),
        ([1, 0, 0, 1, 0, 1], 2, "Multiple zeros, delete one `0` to get [1,1]"),
        ([1, 0], 1, "Array of [1, 0], delete `0` to get [1]"),
        ([1], 0, "Single element 1, delete it to get empty array"),
        ([1, 1, 1, 0, 1, 1, 1], 6, "Delete `0` to get [1, 1, 1, 1, 1, 1]"),
        ([1, 0, 0, 1, 1, 1], 3, "Delete one `0` to get [1,1,1,1]"),
        ([1, 0, 0, 1], 1, "Delete one `0` to get [1, 1, 1]"),
    ]

    # Open the file in write mode
    with open("test results 1493 Longest Subarray of 1 s After Deleting One Element.txt", "w") as file:
        # Loop through the test cases and write the results to the file
        for idx, (nums, expected, description) in enumerate(test_cases):
            result = solution.longestSubarray(nums)
            file.write(f"Test {idx + 1}: {description}\n")
            file.write(f"Input: {nums}\n")
            file.write(f"Expected Output: {expected}\n")
            file.write(f"Output: {result}\n")
            file.write(f"{'Pass' if result == expected else 'Fail'}\n\n")

# Run all test cases and write the results to a file
test_all_cases()
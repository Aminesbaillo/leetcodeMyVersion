def select_subarrays(nums, minK, maxK):
    result = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i, n):
            subarray = nums[i:j+1]
            if min(subarray) == minK and max(subarray) == maxK:
                result.append(subarray)
    
    return result

# Example usage:
nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
result = select_subarrays(nums, minK, maxK)
print(result)

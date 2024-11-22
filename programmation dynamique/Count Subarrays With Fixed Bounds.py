
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        right = 0
        left = 0
        min_val = float('inf')
        max_val = float('-inf')

        while right < n:
            min_val = min(min_val, nums[right])
            max_val = max(max_val, nums[right])

            if min_val == minK and max_val == maxK:
                if min_val == max_val or min_val == nums[right] or max_val == nums[right] :
                    count += right - left +1
                else :        
                    count += 1


            elif max_val > maxK :
                while left <=right : 
                    left+=1
                    max_val = float('-inf')
                    min_val = float('inf')
            elif min_val < minK:
                while left <=right : 
                    left+=1
                    min_val = float('inf')
                    max_val = float('-inf')
            right += 1
        return count

# Test case:
num =  [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913]
kmin = 35054
kmax = 945315
solution = Solution()
d= solution.countSubarrays(num, kmin, kmax )
print("Total count of subarrays:", d)

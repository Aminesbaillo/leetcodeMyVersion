class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        count = 0 
        i= 0 
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                nums.append("")
                count += 1
            else: 
                i += 1
        
        return (n - count),nums
    
solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2],2))
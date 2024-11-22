
        
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        good_subarrays = []
        nu = len(nums)
        unique_value = list(set(nums))
        for i in range(0, nu-k+1):
            d = []
            j = i
            if j != nu-1 and nums[j] == nums[j+1]:
                d.append(nums[j+1])
                j = j+1
            s = nums.index(unique_value[k-1])
            d.extend(nums[i] for i in range(i, s+1))
            while len(set(d)) == k and  s != nu-1 :
                d.append(nums[s])
                good_subarrays.append(d)
                if  nums[s + 1] in d :
                    s += 1 
                else:
                     break 
                
        return len(good_subarrays)  
        
nums = [1,2,1,2,3]
k = 2  
solution = Solution()
print(solution.subarraysWithKDistinct(nums, k))


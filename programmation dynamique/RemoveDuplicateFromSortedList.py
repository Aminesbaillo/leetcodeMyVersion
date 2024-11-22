class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
          stack = [nums[0]]
          for element in nums : 
              if element != stack[-1]:
                  stack.append(element)
              else : 
                  continue 
        else :
          return 0, nums

        numberOfUniqueNums = len(stack)
        nums = stack + [ str('_')for i in range(len(nums)-len(stack))]
        return numberOfUniqueNums,len(nums), nums
    
solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]
))
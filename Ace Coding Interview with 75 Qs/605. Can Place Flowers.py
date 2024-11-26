 
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        total = len(flowerbed)
        for i in range(total):
            if n == 0:
                return True   
            if flowerbed[i] == 0:
                # left plant :
                check_left = (i==0 or flowerbed[i-1] == 0)
                # right plant :
                check_right = (i == total-1 or flowerbed[i+1] == 0)
                if check_left and check_right:
                    flowerbed[i] = 1
                    n -= 1
                 
        return n == 0


# test the function

solution = Solution()
# print(solution.canPlaceFlowers([1,0,0,0,0,1], 2))
print(solution.canPlaceFlowers([0,0,0,0,0,1,0,0], 0))
# print(solution.canPlaceFlowers([1,0,0,0,1], 1))
 
import time 

strat_time = time.time()
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        columns_lists = []
        count = 0
        for j in range(n):
            column = []
            for i in range(n):
                column.append(grid[i][j])
            columns_lists.append(column)

            if column in grid :
                count += grid.count(column)
        return count

# Test the function

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
solution = Solution()
print(solution.equalPairs(grid)) # Output: 3


    
end_time = time.time()
print(f"Execution time: {end_time - strat_time} seconds")
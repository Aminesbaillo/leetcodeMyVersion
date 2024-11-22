# class Solution(object):
#     def islandPerimeter(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         rows, cols = len(grid), len(grid[0])
#         path = set()
#         perimetre = 0
#         def serch(r,c):
#             if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == 0) :
#                 return 1
#             if grid[r][c] == 1 :
#                 grid[r][c] = 2
#                 return serch(r-1, c)+serch(r, c-1)+serch(r+1, c)+serch(r, c+1)
#             return 0

#         for r in range (rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     perimetre += serch(r, c)
                

#         return perimetre 


# class Solution(object):
#     def islandPerimeter(self, grid):
#         """
#         Calculate the perimeter of an island represented by a 2D grid.

#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         rows, cols = len(grid), len(grid[0])
#         perimeter = 0
        
#         # Define a recursive function to explore the island
#         def search(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
#                 # If out of bounds or water encountered, contribute to perimeter
#                 return 1
#             if grid[r][c] == 1:
#                 # Mark this cell as visited (land)
#                 grid[r][c] = 2
#                 # Recursively explore all adjacent land cells
#                 return (search(r - 1, c) +
#                         search(r, c - 1) +
#                         search(r + 1, c) +
#                         search(r, c + 1))
#             return 0

#         # Iterate through each cell in the grid
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:  # If land cell is found
#                     perimeter += search(r, c)  # Calculate perimeter starting from this cell

#         return perimeter
class Solution(object):
    def islandPerimeter(self, grid):
        """
        Calculate the perimeter of an island represented by a 2D grid.

        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        def is_water(r, c):
            # Helper function to determine if a cell is water or out of bounds
            return r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0
        
        def dfs(r, c):
            # Depth-first search (DFS) to traverse the island and calculate perimeter
            if is_water(r, c):
                return 1  # Boundary found, contribute to perimeter
            
            if grid[r][c] == 2:
                return 0  # Already visited
            
            # Mark the cell as visited
            grid[r][c] = 2
            
            # Explore all four directions (up, left, down, right)
            perimeter = (dfs(r - 1, c) +
                         dfs(r, c - 1) +
                         dfs(r + 1, c) +
                         dfs(r, c + 1))
            
            return perimeter
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # Found land, start DFS from here
                    perimeter += dfs(r, c)
        
        return perimeter
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]    
solution = Solution()
print(solution.islandPerimeter(grid))
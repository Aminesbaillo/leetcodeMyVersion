def rotten_fresh_positions_numbers(grid):
  n = len(grid)
  m = len(grid[0])
  position_rotten = []
  count = 0
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 2 :
        position_rotten.append((i, j))
      elif grid[i][j] == 1:
        count += 1
  # print(f"list of rotten positions: {position_rotten}")
  # print(f"total number of fresh oranges: {count}")
  return position_rotten


from collections import deque
def bfs(grid, position_rotten):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque(position_rotten)
    visited = set()
    count = 0
    while queue:
    # print(queue)
        for _ in range(len(queue)):
            i, j = queue.popleft()
            visited.add(grid[i][j])
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and y >= 0 :
                    if grid[x][y] == 1 :
                        grid[x][y] = 2
                        queue.append((x, y))
                    else : 
                        visited.add(grid[x][y])
        count += 1
    return count
# test the function 
grid = [[2,1,1],[1,1,0],[0,1,1]]
position_rotten = rotten_fresh_positions_numbers(grid)
bfs(grid, position_rotten=position_rotten)

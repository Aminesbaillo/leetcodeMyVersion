class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        def find_exit(maze, entrance):
            n, m = len(maze), len(maze[0])
            exits = set()
            for i in range(n):
                for j in range(m):
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        if maze[i][j] == '.' and (i, j) != tuple(entrance):
                            exits.add((i, j))
            return exits

        exit_points = find_exit(maze, entrance)

        def bfs(maze, entrance, exit_points):
            from collections import deque
            queue = deque([(entrance[0], entrance[1], 0)])  # row, col, steps
            visited = set([(entrance[0], entrance[1])])  # Mark entrance as visited
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

            while queue:
                row, col, steps = queue.popleft()

                # Explore all neighbors
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # Check if neighbor is valid
                    if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
                        if maze[new_row][new_col] != '+' and (new_row, new_col) not in visited:
                            # Check if it's an exit
                            if (new_row, new_col) in exit_points:
                                return steps + 1
                            
                            # Add neighbor to queue
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col, steps + 1))

            return -1  # No exit found

        return bfs(maze, entrance, exit_points)

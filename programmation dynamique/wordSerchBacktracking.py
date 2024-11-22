class Solution(object):
    def exist(self, board, word):
        """
        Determine if the given word exists on the board by checking all possible paths.

        :type board: List[List[str]]
            The 2D board (matrix) of characters.
        :type word: str
            The word to search for on the board.
        :rtype: bool
            Returns True if the word exists on the board, otherwise False.
        """
        # Get the number of rows and columns in the board
        rows, cols = len(board), len(board[0])

        # Set to keep track of visited positions
        path = set()

        # Helper function for depth-first search (DFS)
        def dfs(r, c, i):
            # Base case: If we have matched all characters in the word
            if i == len(word):
                return True
            
            # Conditions for backtracking:
            # - Out of bounds (r, c)
            # - Already visited (r, c)
            # - Current character does not match the expected character in the word
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in path or
                word[i] != board[r][c]):
                return False

            # Mark the current position as visited
            path.add((r, c))

            # Recursively explore neighbors in all four directions (up, down, left, right)
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # Backtrack: Unmark the current position as visited
            path.remove((r, c))

            return res

        # Iterate through all positions on the board to start the DFS search
        for r in range(rows):
            for c in range(cols):
                # If DFS from the current position returns True, the word exists on the board
                if dfs(r, c, 0):
                    return True

        # If no valid path is found, return False
        return False

# # Example usage:
solution = Solution()
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
# print(solution.exist(board, word))

board_complex = [
    ["A", "Z", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "Z", "E"],
    ["B", "E", "C", "E"]
]
word_complex = "ZE"

print(solution.exist(board_complex, word_complex))
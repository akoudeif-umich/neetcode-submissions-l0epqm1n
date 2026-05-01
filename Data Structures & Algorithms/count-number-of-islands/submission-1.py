class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        ROWS, COLS = len(grid), len(grid[0])

        num_islands = 0

        def dfs(r, c):

            grid[r][c] = "0"

            for dr, dc in DIRECTIONS:
                row, col = r + dr, c + dc

                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == "1":
                    dfs(row, col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1

        return num_islands
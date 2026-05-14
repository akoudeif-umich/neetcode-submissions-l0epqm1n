class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(-1, 0), (1,0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0


        def dfs(row, col):
            grid[row][col] = "0"


            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                    dfs(r, c)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1

        return num_islands
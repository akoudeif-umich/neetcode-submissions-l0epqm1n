class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        DIRECTIONS = [(-1, 0), (0, -1)]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                curr = 0
                for dr, dc in DIRECTIONS:
                    temp_r, temp_c = row + dr, col + dc
                    if 0 <= temp_r < m and 0 <= temp_c < n:
                        curr += grid[temp_r][temp_c]

                grid[row][col] = curr
        return grid[m - 1][n - 1]
                

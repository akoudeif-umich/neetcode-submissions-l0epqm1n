class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # directions 
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        ROWS, COLS = len(grid), len(grid[0])

        # num islands
        num_islands = 00

        # stack 
        stack = []

        # nested loop through matrix 
        for r in range(ROWS):
            for c in range(COLS):
                # if we hit a 1 (island) dfs or bfs 
                if grid[r][c] == "1":
                    stack.append((r, c))
                    grid[r][c] = "0"
                    num_islands += 1
                
                while stack:
                    curr_r, curr_c = stack.pop()
                    for dr, dc in DIRECTIONS:
                        if curr_r + dr >= 0 and curr_r + dr < ROWS and curr_c + dc < COLS and curr_c + dc >= 0 and grid[curr_r + dr][curr_c + dc] == "1":
                            stack.append((curr_r + dr, curr_c + dc))
                            grid[curr_r + dr][curr_c + dc] = "0"
                    

        return num_islands
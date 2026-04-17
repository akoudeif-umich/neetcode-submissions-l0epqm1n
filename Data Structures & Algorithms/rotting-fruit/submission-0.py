class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        mins = 0 
        num_fresh = 0

        dq = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    dq.append([r, c])
        
        while dq and num_fresh > 0:
            for _ in range(len(dq)):

                curr_r, curr_c = dq.popleft()

                if curr_r + 1 < ROWS and grid[curr_r + 1][curr_c] == 1:
                    num_fresh -= 1
                    grid[curr_r + 1][curr_c] = 2
                    dq.append([curr_r + 1, curr_c])
                if curr_r - 1 >= 0 and grid[curr_r - 1][curr_c] == 1:
                    num_fresh -= 1
                    grid[curr_r - 1][curr_c] = 2
                    dq.append([curr_r - 1, curr_c])
                if curr_c + 1 < COLS and grid[curr_r][curr_c + 1] == 1:
                    num_fresh -= 1
                    grid[curr_r][curr_c + 1] = 2
                    dq.append([curr_r, curr_c + 1])
                if curr_c - 1 >= 0 and grid[curr_r][curr_c - 1] == 1:
                    num_fresh -= 1
                    grid[curr_r][curr_c - 1] = 2
                    dq.append([curr_r, curr_c - 1])
            mins += 1

        if num_fresh == 0:
            return mins

        return -1

        



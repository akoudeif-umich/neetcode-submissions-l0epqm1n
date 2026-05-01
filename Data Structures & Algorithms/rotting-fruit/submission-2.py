class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        need to know how many fresh fruits there are or 
        loop through at the end to check for 1's


        since we rott all neighbors before incrementing min bfs

        need a queue 

        time complexity: O(n^2) for nested loop
        space complexity: O(n) for queue
        """
        # directions list
        DIRECTIONS = [(-1,0), (1,0), (0,1), (0,-1)]

        #rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # queue
        q = deque()

        # count fresh fruit append rotten fruit to queue
        time = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # while queue
        while q and fresh > 0:
            # for rotten fruit in queue:
            for i in range(len(q)):
                row, col = q.popleft()
                # check up down left right
                for dr, dc in DIRECTIONS:
                    temp_r, temp_c = row + dr, col + dc
                    # if fruit rott add to queue and -= fresh fruit
                    if 0 <= temp_r < ROWS and 0 <= temp_c < COLS and grid[temp_r][temp_c] == 1:
                        q.append((temp_r, temp_c))
                        grid[temp_r][temp_c] = 2
                        fresh -= 1


            # increment time 
            time += 1

        # if freshfruit > 0 return -1 else return min
        if fresh > 0:
            return -1
        else:
             return time

    
        


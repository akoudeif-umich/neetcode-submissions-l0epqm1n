class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        0 : empty
        1 : fresh fruit
        2 : rotten fruit

        Directions: up down right left


        1 1 0 
        2 0 1
        0 0 2 

        breadth first search 

        queue [starting rotten]

        first loop and find the fresh and rotten fruit 

        bfs to rott all neighbors 
        count minutes each time 


        check if any fresh fruit left 
        """

        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        ROWS, COLS = len(grid), len(grid[0])

        # deque for rotten fruit
        q = deque()

        # number of fresh fruits
        fresh_fruit = 0

        # minutes 
        mins = 0

        # loop find rotten and fresh fruits
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_fruit += 1
                elif grid[row][col] == 2:
                    q.append((row, col))


        # while q: 
        while q and fresh_fruit > 0: 
            # loop through current items in the queue:
            for i in range(len(q)):
                # pop top of queue 
                row, col = q.popleft()
                # check its neighbors if fresh: 
                for dr, dc in DIRECTIONS:
                    temp_r, temp_c = dr + row, dc + col

                    if 0 <= temp_r < ROWS and 0 <= temp_c < COLS and grid[temp_r][temp_c] == 1:
                        # add to the queue 
                        q.append((temp_r, temp_c))
                        # rott the fruit 
                        grid[temp_r][temp_c] = 2
                        # -= fresh fruit
                        fresh_fruit -= 1

            # increment mins
            mins += 1

        # if fresh fruit > 0 return -1 else return mins 
        return -1 if fresh_fruit else mins












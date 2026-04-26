class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes = 0 
        number_of_fresh_fruits = 0

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            nonlocal minutes
            nonlocal number_of_fresh_fruits 

            if not r in range(ROWS) or not c in range(COLS) or grid[r][c] != 1:
                return 
            
            grid[r][c] = 2
            q.append([r,c])
            number_of_fresh_fruits -= 1



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    number_of_fresh_fruits += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        while q and number_of_fresh_fruits > 0:
            for i in range(len(q)): 
                r,c = q.popleft()
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r, c+1)
                bfs(r, c-1)
            minutes+=1
        
        return minutes if number_of_fresh_fruits == 0 else -1




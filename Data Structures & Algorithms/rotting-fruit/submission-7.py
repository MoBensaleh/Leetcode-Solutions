class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                
            
        if fresh_count == 0:
            return 0
        
        minutes = 0
        directions = [(-1, 0), (1,0), (0,-1), (0,1)]

        while queue and fresh_count > 0:
            level_size = len(queue)

            for _ in range(level_size):
                row, col = queue.popleft()
                for row_offset, col_offset in directions:
                    next_row = row + row_offset
                    next_col = col + col_offset

                    if next_row not in range(ROWS) or next_col not in range(COLS):
                        continue
                    
                    if grid[next_row][next_col] != 1:
                        continue
                    grid[next_row][next_col] = 2
                    fresh_count -= 1
                    queue.append((next_row, next_col))
            minutes += 1

        return minutes if fresh_count == 0 else -1






class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        queue = deque()

        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        minutes = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh_count > 0:
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr not in range(rows) or nc not in range(cols):
                        continue
                    

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1

                        queue.append((nr,nc))
            minutes += 1

        
        if fresh_count > 0: 
            return -1

        return minutes


#
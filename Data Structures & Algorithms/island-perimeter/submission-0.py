class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0
            
            visit.add((r,c))
            perim = dfs(r+1, c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return perim
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c)
        return 0

            



        
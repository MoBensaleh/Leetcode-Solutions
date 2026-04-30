class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        island_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.dfs(r, c, grid, ROWS, COLS)

                    island_count += 1
        return island_count


    def dfs(self, r: int, c: int, grid: List[List[str]], rows: int, cols: int):
        if r not in range(rows) or c not in range(cols):
            return
        
        if grid[r][c] != "1":
            return
        
        grid[r][c] = "0"

        self.dfs(r-1, c, grid, rows, cols)
        self.dfs(r+1, c, grid, rows, cols)
        self.dfs(r, c-1, grid, rows, cols)
        self.dfs(r, c+1, grid, rows, cols)

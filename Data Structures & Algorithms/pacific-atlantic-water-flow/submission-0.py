class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        res = []

        def dfs(r,c,oceanSet,prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in oceanSet or prevHeight > heights[r][c]:
                return
            oceanSet.add((r,c))
            dfs(r+1, c, oceanSet, heights[r][c])
            dfs(r-1, c, oceanSet, heights[r][c])
            dfs(r, c+1, oceanSet, heights[r][c])
            dfs(r, c-1, oceanSet, heights[r][c])

        
        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS-1, col, atl, heights[ROWS-1][col])
        
        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS-1, atl, heights[row][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res

        


        
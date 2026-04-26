class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c, i):
            if i == len(word):
                return True

            if r not in range(ROWS) or c not in range(COLS) or board[r][c] == '#' or word[i] != board[r][c]:
                return False
            board[r][c] = '#'

            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or 
                   dfs(r, c-1, i+1)
            )
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False



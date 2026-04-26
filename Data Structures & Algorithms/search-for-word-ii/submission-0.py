class TrieNode:
    def __init__(self):

        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str):
        root = self

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()

            root = root.children[c]
        root.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()

        path, res = set(), set()

        for word in words:
            root.addWord(word)

        def backtrack(r,c,node, word):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in path or board[r][c] not in node.children:
                return
            
            path.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]

            if node.endOfWord:
                res.add(word)

            backtrack(r+1, c, node, word)
            backtrack(r-1, c, node, word)
            backtrack(r, c+1, node, word)
            backtrack(r, c-1, node, word)
            path.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")
        return list(res)
        
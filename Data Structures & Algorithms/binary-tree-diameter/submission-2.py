# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr):
            if not curr:
                return 0

            nonlocal res
            left=dfs(curr.left)
            right = dfs(curr.right)

            res = max(res, right+left)

            return 1+max(right, left )
        dfs(root)
        return res
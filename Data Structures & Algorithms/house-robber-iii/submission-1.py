# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0,0]

            leftSubTree = dfs(root.left)
            rightSubTree = dfs(root.right)

            withRoot = root.val + leftSubTree[1] + rightSubTree[1]
            withoutRoot = max(leftSubTree) + max(rightSubTree)

            return [withRoot, withoutRoot]

        return max(dfs(root))
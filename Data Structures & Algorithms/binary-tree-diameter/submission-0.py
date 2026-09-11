# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        def dfs(root):
            nonlocal width
            if not root:
                return 0
            dpth_l = dfs(root.left)
            dpth_r = dfs(root.right)

            width = max(width, dpth_l + dpth_r)
            return 1 + max(dpth_l, dpth_r)
        
        dfs(root)
        return width
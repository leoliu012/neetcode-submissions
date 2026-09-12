# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(tree):
            nonlocal balanced
            if not tree:
                return 0
            l_dpth = dfs(tree.left)
            r_dpth = dfs(tree.right)

            print(l_dpth, r_dpth)

            if abs(l_dpth-r_dpth) > 1:
                print(888, l_dpth, r_dpth)
                balanced = False
            
            return 1 + max(l_dpth, r_dpth)
        dfs(root)
        return balanced
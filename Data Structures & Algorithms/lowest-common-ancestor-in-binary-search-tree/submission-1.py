# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(tree):
            if not tree:
                return
            if p.val < tree.val and q.val < tree.val:
                return dfs(tree.left)
            elif p.val > tree.val and q.val > tree.val:
                return dfs(tree.right)
            else:
                return tree
        return dfs(root)

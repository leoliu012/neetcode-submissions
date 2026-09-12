# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(tree):
            print(222, tree.val)
            if not tree:
                print(888)
                return
            if p.val < tree.val and q.val < tree.val:
                print(tree.val)
                return dfs(tree.left)
            elif p.val > tree.val and q.val > tree.val:
                print(tree.val)
                return dfs(tree.right)
            else:
                print(00000, tree.val)
                return tree
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def dfs(tree1, tree2):
            nonlocal same
            if (tree1 == None and tree2) or (tree2 == None and tree1):
                same = False
                return
            if (tree1 == None and tree2 == None):
                return
            if (tree1.val != tree2.val):
                same = False
                return
            if tree1:
                dfs(tree1.left, tree2.left)
                dfs(tree1.right, tree2.right)
            return 
        dfs(p,q)
        return same

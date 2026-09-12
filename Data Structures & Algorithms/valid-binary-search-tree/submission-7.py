# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree, curr_left_boundary, curr_right_boundary):
            if not tree:
                return True
            if tree.val <= curr_left_boundary:
                return False
            if tree.val >= curr_right_boundary:
                return False

            return (dfs(tree.left, curr_left_boundary, tree.val) and 
                    dfs(tree.right, tree.val, curr_right_boundary))
        return dfs(root, float('-inf'), float('inf'))
            
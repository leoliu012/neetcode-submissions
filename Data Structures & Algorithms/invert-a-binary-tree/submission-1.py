# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root:
                tmp = root.left
                root.left = root.right
                root.right = tmp
                invert(root.left)
                invert(root.right)
            else:
                return root
        ret = root
        invert(root)
        return ret
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_ = k
        ret = None
        def dfs(tree):
            nonlocal k_, ret
            if not tree or ret != None:
                return 
            dfs(tree.left)

            if ret is not None:
                return

            if k_ == 1 and ret == None:
                ret = tree.val
            else:
                k_ -= 1
            
            dfs(tree.right)

        dfs(root)
        return ret
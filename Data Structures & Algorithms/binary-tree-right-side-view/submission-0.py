# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        max_d = 0
        def dfs(node, depth):
            nonlocal max_d
            if not node:
                return
            depth += 1
            if depth > max_d:
                print(depth, max_d)
                ret.append(node.val)
                max_d = depth
            dfs(node.right, depth)
            dfs(node.left, depth)
        
        dfs(root, 0)
        return ret
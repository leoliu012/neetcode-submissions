# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        
        if root:
            queue = deque([root])
            vals = deque([root.val])
            while queue:
                node = queue.popleft()
                val = vals.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    if node.val >= val:
                        ret += 1
                        vals.append(node.val)
                        vals.append(node.val)
                    else:
                        vals.append(val)
                        vals.append(val)
        
            
        return ret
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         def invert(root: Optional[TreeNode]) -> Optional[TreeNode]:
#             if root:
#                 tmp = root.left
#                 root.left = root.right
#                 root.right = tmp
#                 invert(root.left)
#                 invert(root.right)
#             else:
#                 return root
#         ret = root
#         invert(root)
#         return ret
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return root
#         q = deque([root])
#         while q:
#             curr_node = q.popleft()
#             curr_node.left, curr_node.right = curr_node.right, curr_node.left
#             if curr_node.left:
#                 q.append(curr_node.left)
#             if curr_node.right:
#                 q.append(curr_node.right)
#         return root
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while stack:
            curr_node = stack.pop()
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
        return root
        
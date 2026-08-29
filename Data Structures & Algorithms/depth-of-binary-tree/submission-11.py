# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         depth = 0
#         q = deque([root])
#         while q:
#             for i in range(len(q)):
#                 curr = q.popleft()
#                 if curr.left:
#                     q.append(curr.left)

#                 if curr.right:
#                     q.append(curr.right)
#             depth += 1
#         return depth

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root, 1]]
        ret = 1
        while stack:
            curr, depth = stack.pop()
            if curr.left:
                stack.append([curr.left, depth+1])
            if curr.right:
                stack.append([curr.right, depth+1])
            ret = max(ret, depth)

        return ret


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(tree1, tree2):
            q1 = deque([tree1])
            q2 = deque([tree2])
            while q1 and q2:
                for _ in range(len(q1)):
                    tree_1 = q1.popleft()
                    tree_2 = q2.popleft()
                    if tree_1 and tree_2 == None:
                        return False
                    if tree_2 and tree_1 == None:
                        return False
                    if (tree_1 == None) and (tree_2 == None):
                        continue
                    
                    if tree_1.val != tree_2.val:
                        return False
                    q1.append(tree_1.left)
                    q1.append(tree_1.right)
                    q2.append(tree_2.left)
                    q2.append(tree_2.right)
            return not q1 and not q2
        
        def dfs(tree, sub):
            if not sub:
                return True
            if not tree:
                return False
            if same_tree(tree, sub):
                return True
            return dfs(tree.left, sub) or dfs(tree.right, sub)
        return  dfs(root, subRoot)
            
                    
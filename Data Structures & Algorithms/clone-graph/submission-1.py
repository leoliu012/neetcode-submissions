"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        visited = dict()
        visited[node] = Node(node.val);
        

        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr_node].neighbors.append(visited[neighbor])

        return  visited[node]
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(-1)
        dummy_p = dummy
        seen = {}
        head_p = head
        while head_p:
            if head_p in seen:
                new_node = seen[head_p]
            else:
                new_node = Node(head_p.val)
                seen[head_p] = new_node

            random_node_old = head_p.random
            if not random_node_old:
                new_node.random = None
            elif random_node_old in seen:
                new_node.random = seen[random_node_old]
            else:
                random_node_new = Node(random_node_old.val)
                seen[random_node_old] = random_node_new
                new_node.random = random_node_new


            dummy_p.next = new_node
            dummy_p = dummy_p.next
            head_p = head_p.next

        new_node.next = None 
        return dummy.next
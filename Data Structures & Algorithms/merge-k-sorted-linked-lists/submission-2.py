# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals_head = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(vals_head, (l.val, i, l))
        ret = ListNode()
        ret_dummy = ret

        while vals_head:
            val, i, l = heapq.heappop(vals_head)
            new = ListNode(val)
            ret.next = new
            ret = ret.next
            if l.next:
                heapq.heappush(vals_head, (l.next.val, i, l.next))
        return ret_dummy.next
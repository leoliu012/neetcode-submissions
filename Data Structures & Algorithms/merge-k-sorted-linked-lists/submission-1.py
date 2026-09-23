# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for l in lists:
            while l:
                heapq.heappush(vals, l.val)
                l = l.next
        ret = ListNode()
        ret_dummy = ret

        while vals:
            val = heapq.heappop(vals)
            new = ListNode(val)
            ret.next = new
            ret = ret.next
        return ret_dummy.next
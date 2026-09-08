# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index_to_pointer = {} #prev, p, next
        head_p = head
        prev = None
        i = 0
        while head_p:
            i += 1
            index_to_pointer[i] = [prev, head_p, head_p.next]
            prev = head_p
            head_p = head_p.next
        print(index_to_pointer)
        del_index = i + 1 - n
        prev_del = index_to_pointer[del_index][0]
        next_del = index_to_pointer[del_index][2]

        print(del_index)
        # print(prev_del.val)
        # print(next_del.val)
        if not prev_del and not next_del:
            return None

        if prev_del and next_del:
            prev_del.next = next_del
            return head
        if prev_del:
            prev_del.next = None
            return head
        if not prev_del:
            return next_del
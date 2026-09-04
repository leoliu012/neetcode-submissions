# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)

        second = slow.next
        slow.next = None
        
        second_p = second
        prev = None
        while second_p:
            tmp = second_p.next
            second_p.next = prev
            prev = second_p
            second_p = tmp
        
        second = prev

        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


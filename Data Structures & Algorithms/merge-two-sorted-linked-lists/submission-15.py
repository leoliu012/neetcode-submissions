# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         ret = ListNode()
#         ret_op = ret
#         curr_node1 = list1
#         curr_node2 = list2
#         while curr_node1 or curr_node2:
#             if not curr_node2:
#                 ret_op.next = curr_node1
#                 break
#             if not curr_node1:
#                 ret_op.next = curr_node2
#                 break
#             val1 = curr_node1.val
#             val2 = curr_node2.val
#             print(val1, val2)
#             if val1<val2:
#                 ret_op.val = val1
#                 curr_node1 = curr_node1.next
#             else:
#                 ret_op.val = val2
#                 curr_node2 = curr_node2.next
#             ret_op.next = ListNode()
#             ret_op = ret_op.next
#         return ret
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curr_node1 = list1
        curr_node2 = list2
        while curr_node1 or curr_node2:
            if not curr_node2:
                tail.next = curr_node1
                break
            if not curr_node1:
                tail.next = curr_node2
                break
            val1 = curr_node1.val
            val2 = curr_node2.val
            if val1<val2:
                tail.next = curr_node1
                curr_node1 = curr_node1.next
            else:
                tail.next = curr_node2
                curr_node2 = curr_node2.next
            tail = tail.next
        return dummy.next
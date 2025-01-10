# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dump = ListNode()
        head = dump
        l1, l2 = list1, list2
        while l1 or l2:
            op1 = l1.val if l1 else float('inf')
            op2 = l2.val if l2 else float('inf')
            got = min(op1, op2)
            dump.next = ListNode(got)
            dump = dump.next
            if op1 <= op2:
                l1 = l1.next
            else:
                l2 = l2.next
            

        return head.next

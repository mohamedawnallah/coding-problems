# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_summed = ListNode()
        head = list_summed
        ptr1, ptr2, carry = l1, l2, 0
        while ptr1 or ptr2:
            current = ptr1.val if ptr1 else 0
            current += ptr2.val if ptr2 else 0
            current += carry
            carry, got = current // 10, current % 10
            list_summed.next = ListNode(got)
            list_summed = list_summed.next
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        if carry > 0:
            list_summed.next = ListNode(carry)

        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        source = dummy

        # Pass1: Get the source node before the left position.
        for _ in range(left-1):
            source = source.next

        # Pass2: Reverse the list starting from left to right inclusive.
        prev, current = None, source.next
        for _ in range(right-left+1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
    
        # Pass3: Connect the reversed part with the rest of the list.
        source.next.next = current
        source.next = prev

        return dummy.next

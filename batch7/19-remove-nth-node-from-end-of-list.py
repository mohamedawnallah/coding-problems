# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Pass 1: Calculate the length of the linkedlist
        total = 0
        current = head
        while current:
            total += 1
            current = current.next

        # Pass 2: Get start index of the node to remove from start position
        node_to_remove_index = total - n
        if node_to_remove_index == 0:
            return head.next

        i = 0
        prev, current = None, head
        while current:
            if i == node_to_remove_index-1:
                prev = current
            if i == node_to_remove_index:
                prev.next = current.next
                current.next = None
            current = current.next
            i += 1
        
        return head

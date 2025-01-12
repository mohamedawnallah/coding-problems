# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        # Pass 1: Compute the length of list.
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Pass 2: Make the list circular.
        current.next = head

        # Pass 3: Compute the new tail and new head.
        k = k % length
        tail = head
        for _ in range(length-k-1):
            tail = tail.next
        head = tail.next
        tail.next = None

        return head

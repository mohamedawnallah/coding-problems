# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Pass 1: Calculate the length of the linkedlist.
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        # Pass 2: Get the end of reverse point pointers for each group if any.
        reverse_points = []
        current = head
        k_groups = n // k
        for _ in range(k_groups):
            for i in range(k):
                if i == k-1:
                    reverse_points.append(current)
                current = current.next

        # Pass 3: Reverse k groups.
        post_reverse_groups = reverse_points[-1].next
        source, current = None, head
        head = reverse_points[0]
        prev = None
        for i in range(len(reverse_points)):
            reverse_point_temp = reverse_points[i].next
            prev = self.reverse(source, current, reverse_points[i])
            source = current
            current = reverse_point_temp

        prev.next = post_reverse_groups

        return head

    def reverse(self, source, start, end):
        prev, current = source, start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        current.next = prev
        if source:
            source.next = current
        return start

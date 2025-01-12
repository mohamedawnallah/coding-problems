"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Pass 1: Create twin list alongside the original list.
        current = head
        while current:
            new_node = Node(current.val, current.next, None)
            current.next = new_node
            current = new_node.next

        # Pass 2: Assign random pointers to the twin list with the same list state.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
    
        # Pass 3: Seperate the twin list from the original list and vice versa.
        current, new_head = head, head.next
        while current:
            new_node = current.next
            current.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            current = current.next

        return new_head

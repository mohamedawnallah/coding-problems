# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sameTree(p1, q1):
            if not p1 and not q1:
                return True
            if not p1 or not q1:
                return False
            if p1.val != q1.val:
                return False
            return sameTree(p1.left, q1.left) and sameTree(p1.right, q1.right)
        return sameTree(p, q)

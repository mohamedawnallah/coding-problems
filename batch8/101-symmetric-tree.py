# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric_sides(left_tree, right_tree):
            if not left_tree and not right_tree:
                return True
            if not left_tree or not right_tree:
                return False
            if left_tree.val != right_tree.val:
                return False
            return is_symmetric_sides(left_tree.left, right_tree.right) and is_symmetric_sides(left_tree.right, right_tree.left)
        return is_symmetric_sides(root.left, root.right)

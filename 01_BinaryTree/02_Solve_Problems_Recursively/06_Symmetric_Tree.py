# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

''' Recursive Method '''


class Solution:
    def mirror(self, left, right):
        if left == None and right == None:
            return True
        if left and right and left.val == right.val:
            return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.mirror(root.left, root.right)

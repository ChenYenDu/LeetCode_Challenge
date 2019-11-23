# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if not root.left and not root.right:
            return 1     # if root is not None but without left and right node return 1

        # recursively calculate the depth of left node
        left_minDepth = self.minDepth(root.left)
        # recursively calculate the depth of right node
        right_minDepth = self.minDepth(root.right)

        if not root.left:  # if left node do not exist, return the mindepth of rigth node + 1
            return right_minDepth+1

        if not root.right:  # if right nodo do not exist, return the mindepth of left node + 1
            return left_minDepth+1

        return min(left_minDepth, right_minDepth)+1
        # if both left and right node exist, return te min of them and +1

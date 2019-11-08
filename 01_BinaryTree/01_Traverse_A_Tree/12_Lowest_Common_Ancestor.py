# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right != None: # this mean vboth side find p or q so the root is the LCA
            return root

        if left == None:   # if left or right return none means there were no p or q in that path
            return right   # pass root to right child if found none in left path
        else:
            return left    # pass root to left child if found none in right path

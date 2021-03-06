# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:  # travel to each node's left child, till reach the left leaf
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()  # this node has no left child
            res.append(cur.val)  # so let's append the node value
            cur = cur.right  # visit its right child --> if it has left child ? append left and left.val, otherwise append node.val, then visit right child again... cur = node.right
        return res

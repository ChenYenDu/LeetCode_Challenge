# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Recursive:
Space Complexity: O(N)
Time Complexity: O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # value of current node or parent node.
        parent_val = root.val
        
        # value of p
        p_val = p.val
        
        # value of q
        q_val = q.val
        
        # if both p and q are greater then parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # if both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # we have found the split point, i.e the LCA node.
        else:
            return root
'''
# Iterative
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q:'TreeNod') -> 'TreeNode':
        # value of p
        p_value = p.val
        
        # value of q
        q_value = q.val
        
        # Start from the root node of the tree
        node = root
        
        # Traverse the tree
        while node:
            
            # value of current node or parent node
            parent_value = node.val
            
            if p_value > parent_value and q_value > parent_value:
                # if both p and q are lesser than parent
                node = node.right
            elif p_value < parent_value and q_value < parent_value:
                node = node.left
            else:
                # we have found the split point, i.e. the LCA node
                return node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Recursive:
Time Complexity: O(n)
Space Complexity: O(n)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
'''
'''
Iterative:
Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root        
        
        
        
        
        
        

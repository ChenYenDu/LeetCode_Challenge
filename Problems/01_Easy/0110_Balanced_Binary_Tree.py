# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
# Solution 1: O(nlogn)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return abs(left_depth-right_depth) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, root):
        if root == None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

"""

# Solution 2: O(n)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.checkBBT(root)[0]

    def checkBBT(self, root):  # 計算左右最大深度的時候同時確認是否同高
        if root == None:
            return True, 0
        isLeftBBT, leftDepth = self.checkBBT(root.left)
        isRightBBT, rightDepth = self.checkBBT(root.right)
        isBBT = isLeftBBT and isRightBBT and abs(leftDepth - rightDepth) <= 1
        depth = max(leftDepth, rightDepth) + 1
        return isBBT, depth

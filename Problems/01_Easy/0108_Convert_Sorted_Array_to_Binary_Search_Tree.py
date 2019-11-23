# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        return self.buildBST(nums, 0, len(nums)-1)

    def buildBST(self, nums, start, end):
        if start > end:
            return None

        # get int value of division to find middle node
        mid = (start + end) // 2

        node = TreeNode(nums[mid])
        # recursive through the left part of middle node
        node.left = self.buildBST(nums, start, mid-1)
        # recursive through the right part of middle node
        node.right = self.buildBST(nums, mid+1, end)

        return node

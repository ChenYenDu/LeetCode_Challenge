# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i  # {9:0, 3:1, 15:2, 20:3, 7:4}
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        # if len(inorder) = 0 return None -> root is None
        if in_start == in_end:
            return None
        # the last value of postorder is "val" of the highest level
        node = TreeNode(postorder[post_end - 1])
        # find the position of the "val" in inorder traversal
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(
            lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        # recall the function with
        node.right = self.buildTreeRecu(
            lookup, postorder, inorder, post_end - 1, i + 1, in_end)
        return node

# mind road:
# inorder split by the element from the in_end,
# double quote for means the element which is taken at the level
#           [9,"3",15,20,7]
#          /             \
#       ["9"]               [15, "20", 7]
#                          /         \
#                       ["15"]          ["7"]

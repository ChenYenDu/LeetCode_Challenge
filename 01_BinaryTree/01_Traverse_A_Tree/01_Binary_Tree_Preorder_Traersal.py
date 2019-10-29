# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            rst = []
            collect = [root]

            while len(collect) > 0:
                stack = collect.pop()
                if stack.val != None:
                    rst.append(stack.val)
                    if stack.right != None:
                        collect.append(stack.right)
                    if stack.left != None:
                        collect.append(stack.left)
            return rst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = []
        cur = root
        prev = None
        while stack or cur:
            while cur:  # similar as inorder stack solution
                stack.append((cur, False))
                cur = cur.left

            # get top of stack, note: we can't simply pop because not sure if leftnode and rightnode are both visited.
            cur, finishedLeft = stack[-1]

            if finishedLeft:  # Left subtree has been finished, so we can pop the stack and append result to res list
                stack.pop()
                res.append(cur.val)
                cur = None
            else:  # Left subtree has not be visited, so we can't pop the current node, because we have to do some work on its right subtree.
                stack.pop()
                stack.append((cur, True))
                cur = cur.right
        return res  # job done. Beat 99% of python submission!

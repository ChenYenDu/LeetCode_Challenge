# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class IterationSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
            come from the solution, but why is this iteration not recrusion
        """

        def check(p, q):
            if not p and not q:  # it p and q ate both None -> return True
                return True
            if not p or not q:   # if any of p or q are None and differ from theother one -> return False
                return False
            if p.val != q.val:   # if both are not Noen , but val differs -> return False
                return False

            deq = deque([(p, q), ])
            while deq:
                p, q = deq.popleft()
                if not check(p, q):
                    return False

                if p:
                    dep.append((p.left, q.left))
                    dep.append((p.right, q.right))

            return True


class RecrusionSoltion:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

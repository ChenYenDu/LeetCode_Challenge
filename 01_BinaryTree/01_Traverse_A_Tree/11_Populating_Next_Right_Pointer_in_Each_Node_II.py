"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return
        root.next = None

        self.connectChildern(root, root.left)
        self.connectChildern(root, root.right)
        return root

    def connectChildern(self, parent, child):
        if child == None or child.next != None:
            return

        if child == parent.left and parent.right != None:
            child.next = parent.right
            self.connectChildern(parent, parent.right)
        else:
            child.next = None
            currP = parent.next
            while currP != None:
                if currP.left != None:
                    child.next = currP.left
                    break
                if currP.right != None:
                    child.next = currP.right
                    break
                currP = currP.next

        self.connectChildern(child, child.left)
        self.connectChildern(child, child.right)

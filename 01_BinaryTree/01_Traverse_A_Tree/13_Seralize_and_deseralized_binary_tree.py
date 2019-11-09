# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []  # create a empty list to save val from root

        def preOrder(root):   # according to the quest we are using preorder traversal here
            if not root:
                vals.append('#')  # append a sharp sign here instead of null
            else:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)            # run preorder function recursively
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(val for val in data.split(
        ))  # split the data in to seperate string list

        def build():                    # create a build tree method for recursive usage
            if vals:
                val = vals.popleft()    # take the first element as root.val
                if val == '#':          # if the first element is # take it as null in the tree
                    return None
                # pass root to the next element in list
                root = TreeNode(int(val))
                root.left = build()        # run the function recursively to make left and right node
                root.right = build()
                return root
        return build()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

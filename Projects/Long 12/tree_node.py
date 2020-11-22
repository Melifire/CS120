"""
    tree_node.py

    Contains a simple TreeNode class
"""

class TreeNode:
    """ Models a single node in a tree. 
    """

    def __init__(self, val):
        """ Constructs the object; caller must pass a value, which will be
            stored in the 'val' field.
        """

        self.val = val
        self.left = None
        self.right = None
        self.subtree_count = 1
        self.depth = 0  # the root node in this class has a height of 0


    def __str__(self):
        if self is None:
            return ''
        else:
            return str(self.left or '') + ' - (' + f'{str(self.val)} {str(self.depth)} {str(self.subtree_count)}' + ') - ' + str(self.right or '')

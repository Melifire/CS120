#! /usr/bin/python3

""" Code to test the tree_count() function

    Author: Russ Lewis
"""

import simple_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(8)
root.left = TreeNode(-27)
root.left.left = TreeNode(41)
root.left.left.left = TreeNode(79)
root.left.left.left.left = TreeNode(-15)
root.left.left.right = TreeNode(-47)
root.left.right = TreeNode(21)
root.left.right.left = TreeNode(24)
root.left.right.left.left = TreeNode(54)
root.left.right.right = TreeNode(5)
root.right = TreeNode(-7)
root.right.left = TreeNode(-16)
root.right.left.left = TreeNode(64)
root.right.left.left.right = TreeNode(14)
root.right.left.left.right.left = TreeNode(85)
root.right.left.right = TreeNode(-25)
root.right.left.right.right = TreeNode(31)
root.right.right = TreeNode(-33)
root.right.right.left = TreeNode(97)
root.right.right.left.right = TreeNode(4)
root.right.right.right = TreeNode(-30)



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_count()...")
    print()

    retval = simple_tree_funcs.tree_count(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



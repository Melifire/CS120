#! /usr/bin/python3

""" Code to test the in_order_traversal_print() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(13)
root.left = TreeNode(26)
root.left.left = TreeNode(-11)
root.left.left.left = TreeNode(80)
root.left.left.left.right = TreeNode(-7)
root.left.left.left.right.right = TreeNode(-32)
root.left.left.right = TreeNode(85)
root.left.right = TreeNode(93)
root.left.right.left = TreeNode(52)
root.left.right.right = TreeNode(67)
root.left.right.right.left = TreeNode(81)
root.left.right.right.left.left = TreeNode(39)
root.left.right.right.left.right = TreeNode(32)
root.right = TreeNode(68)
root.right.left = TreeNode(75)
root.right.left.left = TreeNode(49)
root.right.right = TreeNode(-1)
root.right.right.left = TreeNode(27)
root.right.right.right = TreeNode(5)



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing in_order_traversal_print()...")
    print()

    retval = advanced_tree_funcs.in_order_traversal_print(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



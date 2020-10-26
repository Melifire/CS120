#! /usr/bin/python3

""" Code to test the bst_max() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(8)

root.left = TreeNode(-27)

root.left.left = TreeNode(-47)
root.left.right = TreeNode(-15)

root.left.left.right = TreeNode(-33)
root.left.left.right.right = TreeNode(-30)

root.left.right.left = TreeNode(-16)

root.left.right.left.left = TreeNode(-25)

root.left.right.right = TreeNode(5)

root.left.right.right.left = TreeNode(-7)

root.left.right.right.left.right = TreeNode(4)

root.right = TreeNode(41)

root.right.left = TreeNode(21)
root.right.right = TreeNode(79)

root.right.left.left  = TreeNode(14)
root.right.left.right = TreeNode(24)

root.right.left.right.right = TreeNode(31)

root.right.right = TreeNode(54)
root.right.right.right = TreeNode(64)
root.right.right.right.right = TreeNode(85)
root.right.right.right.right.right = TreeNode(97)

#vals = advanced_tree_funcs.in_order_vals(root)
#print(vals)
#print(sorted(vals))
#assert sorted(vals) == vals



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing bst_max()...")
    print()

    retval = advanced_tree_funcs.bst_max(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



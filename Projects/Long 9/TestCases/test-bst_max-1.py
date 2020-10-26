#! /usr/bin/python3

""" Code to test the bst_max() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)

root.left  = TreeNode(-31)
root.right = TreeNode(52)

root.left.left  = TreeNode(-50)
root.left.right = TreeNode(-25)

root.right.left  = TreeNode(12)
root.right.right = TreeNode(66)

root.right.left.left  = TreeNode(-17)
root.right.left.right = TreeNode(50)

root.right.left.left.right = TreeNode(4)

root.right.left.left.right.left  = TreeNode(-6)
root.right.left.left.right.right = TreeNode(9)

root.right.left.right.left = TreeNode(40)

root.right.left.left.right = TreeNode(-12)

root.right.left.right.left  = TreeNode(34)

root.right.left.right.left.left = TreeNode(26)

root.right.left.right.left.left.left = TreeNode(25)

root.right.right.right = TreeNode(81)

root.right.right.right.left  = TreeNode(77)
root.right.right.right.right = TreeNode(83)

root.right.right.right.left.right = TreeNode(80)

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



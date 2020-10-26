#! /usr/bin/python3

""" Code to test the bst_max() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-31)
root.right = TreeNode(-19)
root.right.right = TreeNode(81)
root.right.right.left = TreeNode(-6)
root.right.right.left.right = TreeNode(77)
root.right.right.left.right.left = TreeNode(66)
root.right.right.left.right.left.left = TreeNode(52)
root.right.right.left.right.left.left.left = TreeNode(12)
root.right.right.left.right.left.left.left.right = TreeNode(50)


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



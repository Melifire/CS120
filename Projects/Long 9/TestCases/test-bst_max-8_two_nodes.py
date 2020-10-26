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
root.right = TreeNode(52)



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



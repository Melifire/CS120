#! /usr/bin/python3

""" Code to test the post_order_traversal_print() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)
root.left = TreeNode(52)



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing post_order_traversal_print()...")
    print()

    retval = advanced_tree_funcs.post_order_traversal_print(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



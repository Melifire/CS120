#! /usr/bin/python3

""" Code to test the in_order_vals() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = None



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing in_order_vals()...")
    print()

    retval = advanced_tree_funcs.in_order_vals(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



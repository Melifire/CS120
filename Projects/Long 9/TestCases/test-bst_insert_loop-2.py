#! /usr/bin/python3

""" Code to test the bst_insert_loop() function

    Author: Russ Lewis
"""

import advanced_tree_funcs

from tree_node import TreeNode



###########################################################
#                       INPUT                             #
###########################################################

vals = [ 13, 26, -11, 80, -7, -32, 85, 93, 52, 67, 81, 39, 32, 68, 75, 49, -1, 27, 5 ]




###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing bst_insert_loop()...")
    print()

    root = TreeNode(vals[0])
    for v in vals[1:]:
        advanced_tree_funcs.bst_insert_loop(root, v)

    print("IN-ORDER TRAVERSAL:")
    advanced_tree_funcs.in_order_traversal_print(root)
    print()

    print("PRE-ORDER TRAVERSAL:")
    advanced_tree_funcs.pre_order_traversal_print(root)
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



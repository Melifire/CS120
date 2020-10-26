#! /usr/bin/python3

""" Code to test the tree_build_left_linked_list() function

    Author: Russ Lewis
"""

import simple_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

vals = [ 13, 26, -11, 80, -7, -32, 85, 93, 52, 67, 81, 39, 32, 68, 75, 49, -1, 27, 5 ]



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_build_left_linked_list()...")
    print()

    root = simple_tree_funcs.tree_build_left_linked_list(vals)

    print("RETURNED TREE:")

    cur = root
    while cur is not None:
        print(f"There is a node with value {cur.val}")

        if cur.right is not None:
            print("ERROR: This node has a right node, that is wrong!!!")
        cur = cur.left

    print()
    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


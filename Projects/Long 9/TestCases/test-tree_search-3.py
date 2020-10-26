#! /usr/bin/python3

""" Code to test the tree_search() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



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
    print("Testing tree_search()...")
    print()

    def test_one(val):
        print(f"Testing with search key = {val}")
        retval = advanced_tree_funcs.tree_search(root, val)
        if retval is None:
            print("    Returned: None")
        else:
            print(f"    Returned: val = {retval.val}")
        print()

    test_one(-7)
    test_one(0)
    test_one(83)
    test_one(32)
    test_one(31)
    test_one(12)
    test_one(-33)
    test_one(1234)
    test_one(-1234)

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



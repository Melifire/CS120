#! /usr/bin/python3

""" Code to test the tree_search() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)
root.left = TreeNode(52)
root.left.left = TreeNode(12)
root.left.left.left = TreeNode(66)
root.left.left.left.right = TreeNode(50)
root.left.left.right = TreeNode(-31)
root.left.left.right.right = TreeNode(81)
root.left.right = TreeNode(-6)
root.left.right.left = TreeNode(77)
root.left.right.right = TreeNode(34)
root.left.right.right.left = TreeNode(26)
root.right = TreeNode(-17)
root.right.left = TreeNode(-12)
root.right.left.left = TreeNode(40)
root.right.left.left.right = TreeNode(80)
root.right.left.left.right.left = TreeNode(4)
root.right.left.right = TreeNode(-25)
root.right.right = TreeNode(25)
root.right.right.left = TreeNode(-50)
root.right.right.right = TreeNode(83)
root.right.right.right.right = TreeNode(9)



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

    test_one(-19)
    test_one(0)
    test_one(83)
    test_one(12)
    test_one(17)
    test_one(12)
    test_one(34)
    test_one(1234)
    test_one(-1234)

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



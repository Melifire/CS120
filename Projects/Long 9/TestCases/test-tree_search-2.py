#! /usr/bin/python3

""" Code to test the tree_search() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(13)
root.left = TreeNode(26)
root.left.left = TreeNode(-11)
root.left.left.left = TreeNode(80)
root.left.left.left.right = TreeNode(-7)
root.left.left.left.right.right = TreeNode(-32)
root.left.left.right = TreeNode(85)
root.left.right = TreeNode(93)
root.left.right.left = TreeNode(52)
root.left.right.right = TreeNode(67)
root.left.right.right.left = TreeNode(81)
root.left.right.right.left.left = TreeNode(39)
root.left.right.right.left.right = TreeNode(32)
root.right = TreeNode(68)
root.right.left = TreeNode(75)
root.right.left.left = TreeNode(49)
root.right.right = TreeNode(-1)
root.right.right.left = TreeNode(27)
root.right.right.right = TreeNode(5)



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

    test_one(13)
    test_one(0)
    test_one(52)
    test_one(13)
    test_one(26)
    test_one(93)
    test_one(34)
    test_one(1234)
    test_one(-1234)

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



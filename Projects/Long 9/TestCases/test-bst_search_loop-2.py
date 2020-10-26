#! /usr/bin/python3

""" Code to test the bst_search_loop() function

    Author: Russ Lewis
"""

import advanced_tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(13)

root.left  = TreeNode(-11)
root.right = TreeNode(26)

root.left.left  = TreeNode(-32)
root.left.right = TreeNode(-7)

root.left.right.right = TreeNode(-1)

root.left.right.right.right = TreeNode(5)

root.right.right = TreeNode(80)

root.right.right.left  = TreeNode(52)
root.right.right.right = TreeNode(85)

root.right.right.left.left  = TreeNode(39)
root.right.right.left.right = TreeNode(67)

root.right.right.left.left.left  = TreeNode(27)
root.right.right.left.left.right = TreeNode(49)

root.right.right.left.right.right = TreeNode(68)

root.right.right.left.right.right.right = TreeNode(75)

root.right.right.left.left.left = TreeNode(32)

root.right.right.right.left = TreeNode(81)
root.right.right.right.right = TreeNode(93)

#vals = advanced_tree_funcs.in_order_vals(root)
#print(vals)
#print(sorted(vals))
#assert sorted(vals) == vals



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing bst_search_loop()...")
    print()

    def test_one(val):
        print(f"Testing with search key = {val}")
        retval = advanced_tree_funcs.bst_search_loop(root, val)
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



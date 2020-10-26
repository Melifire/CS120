#! /usr/bin/python3

""" Code to test the bst_search_loop() function

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

    test_one(-19)
    test_one(0)
    test_one(83)
    test_one(-31)
    test_one(17)
    test_one(12)
    test_one(50)
    test_one(1234)
    test_one(-1234)

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



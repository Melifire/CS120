#! /usr/bin/python3

""" Code to test the tree_search() function

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



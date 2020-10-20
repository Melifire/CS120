#! /usr/bin/python3

""" Code to test the append_list_to_list() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import proj05_short





###########################################################
#              INPUT AND EXPECTED OUTPUT                  #
###########################################################
# INPUT:
#   First, we build two lists of nodes.
#   Then we chain each together.
nodes1 = [ list_node.ListNode(2),
           list_node.ListNode(3),
           list_node.ListNode(5),
           list_node.ListNode(7),
           list_node.ListNode(11),
           list_node.ListNode(13),
           list_node.ListNode(17),
           list_node.ListNode(19)  ]

nodes2 = [ list_node.ListNode("abc"),
           list_node.ListNode("def"),
           list_node.ListNode("ghi"),
           list_node.ListNode("jkl"),
           list_node.ListNode("mno"),
           list_node.ListNode("pqrs"),
           list_node.ListNode("tuv"),
           list_node.ListNode("wxyz") ]

in_list1 = nodes1[0]
nodes1[0].next = nodes1[1]
nodes1[1].next = nodes1[2]
nodes1[2].next = nodes1[3]
nodes1[3].next = nodes1[4]
nodes1[4].next = nodes1[5]
nodes1[5].next = nodes1[6]
nodes1[6].next = nodes1[7]

in_list2 = nodes2[0]
nodes2[0].next = nodes2[1]
nodes2[1].next = nodes2[2]
nodes2[2].next = nodes2[3]
nodes2[3].next = nodes2[4]
nodes2[4].next = nodes2[5]
nodes2[5].next = nodes2[6]
nodes2[6].next = nodes2[7]

# EXPECTED OUTPUT:
#   The *nodes* that we expect as the output list.  Note that we don't need to
#   explicitly check that the contents are correct (and unchanged in each
#   node), since the list-printout will implicitly check that.  But we *do*
#   want to assert that the *nodes* are in exactly the order we expect.  If
#   they aren't (but we pass the value check), then this means that the
#   student was moving values around between nodes (or, creating new nodes).
expected_out_list = nodes1+nodes2



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing append_list_to_list()...")
    print()
    print(f"Input list 1: {in_list1}")
    print(f"Input list 2: {in_list2}")

    out_list = proj05_short.append_list_to_list(in_list1, in_list2)

    print(f"Returned list: {out_list}")
    print()

    print("Checking to make sure that all of the nodes in the output list are")
    print("from the input list.  If you see a failure reported here, then")
    print("it's likely that you did one or more of the following:")
    print("   - Created new nodes, instead of just changing the references")
    print("   - Swapped values between nodes")
    print(" ... Checking ...")

    # check that the returned value is a list
    curr  = out_list
    count = 0

    while curr is not None:
        if not isinstance(curr, list_node.ListNode):
            print("ERROR: One or more nodes is not of the ListNode class.  NOTE: This can happen if you copy the ListNode class into your own file, instead of using the version inside list_node.py")
            break
        
        if curr not in nodes1 and curr not in nodes2:
            print("ERROR: One of the nodes in the list that you returned was not from the original, input list.  This means that you were creating new nodes.")
            break

        if curr not in expected_out_list:
            print("ERROR: One of the nodes in the list that you returned was supposed to have been removed; it was in the original list, but was not supposed to be in the result.")
            break
        
        if curr is not expected_out_list[count]:
            print("ERROR: One of the nodes in the list that you returned was from the input list, but it's not in the correct position.  Probably, this means you didn't reverse the list properly.  It's also possible that you tried to swap *values*, instead of moving the nodes around.")
            break
        
        curr   = curr.next
        count += 1

    print("Output list node check complete.")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()



"""list_insert.py - A couple of simple list functions

Author: Russ Lewis

Declares sorted_list_insert() and list_print(), both of which are fairly
simple list functions.  This exists primarily as a set of code that
students will use to practice doing code coverage.

Note that the insert function assumes that every value inserted is a two
element tuple, where the second element is the primary search key, and the
first element is a secondary search key.

ALSO NOTE: This is intentionally suboptimal code!  To make the code coverage
           problem a little more interesting, I have *intentionally* split,
           into multiple cases, things which I ordinarily would combine into
           simpler, unified cases!
"""



class ListNode:
    def __init__(self, val):
        assert type(val) == tuple
        assert len(val) == 2
        self.val  = val
        self.next = None


def sorted_list_insert(old_head, new_node):
    if old_head is None:
        return new_node

    # if this was your code, you should have a comment here.  But I'm
    # leaving it for an exercise for you: what does this test check for?
    # Why does it ignore element [0] of the tuples?

    if new_node.val[1] < old_head.val[1]:
        # you would write a comment here: what is this doing?  What is the
        # shape of the list after this is done?

        new_node.next = old_head
        return new_node

    # you would write a comment here: what is this checking for?  Why is
    # this comparing both elements, whereas the one above did not?  Why
    # is it using <= in the second test?

    if new_node.val[1] == old_head.val[1]:
        if new_node.val[0] <= old_head.val[0]:
            new_node.next = old_head
            return new_node


    # you would write a comment here: what is 'cur' ?  And what is the
    # loop condition?  When does the loop end, and what will you know to
    # be true when it ends?

    cur = old_head
    while True:
        if cur.next is None:
            break

        if new_node.val[1] < cur.next.val[1]:
            break

        if new_node.val[1] == cur.next.val[1]:
            if new_node.val[0] <= cur.next.val[0]:
                break


        cur = cur.next


    # you would write a comment here: what do you know to be true about
    # 'cur', in relation to the rest of the list - and also in relation
    # to new_node?

    new_node.next = cur.next
    cur.next = new_node

    return old_head



def print_list(head):
    print("--- Beginning linked list printout... ---")

    if head == None:
        print("  <list is empty>")
    else:
        cur = head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    print("--- done ---")
    print()




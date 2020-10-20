""" File: proj05_long.py
    Author: Ben Kruse
    Purpose: Performs various functions on linked lists
"""

from list_node import ListNode

def is_sorted(head):
    # recursivly makes sure the head nodes value is <= the head of the linked 
    # list in contains
    if head and head.next:
        return head.val <= head.next.val and is_sorted(head.next)
    else:
        return True  # if the node does not contain another list, return True

def list_sum(head):
    # recursivly adds the head nodes value to this function called on the list
    # it contains
    if head:
        return head.val + list_sum(head.next)
    else:
        return 0  # if there is no more list, return 0 to end recursion

def partition_list(head):
    if not head:  # checks for an empty input
        return (None, None)
    
    head2 = head.next  # starts our second list
    cur = head         # cur and cur2 used to loop through list and set values
    cur2 = head2       # for head and head2 respectivly

    while cur and cur.next:
        cur.next = cur.next.next
        # checks for possible error will end of list and avoids. This is used
        # rather than a change to the while condition because for odd length
        # lists, head is added to once more than head2
        if cur2.next:  
            cur2.next = cur.next.next
        cur = cur.next
        cur2 = cur2.next
    return (head, head2)

def accordion_n(head, skip_amt):
    # the placeholder is used to keep code consistant: the first value returned
    # is skip_amt after a zeroth node, here refered to as placeholder
    placeholder = ListNode("Placeholder")
    placeholder.next = head  
    head = placeholder  # makes the head point to the placeholder
    cur = head
    while cur:
        for _ in range(skip_amt):  # moves cur.next forward skip_amt times
            if cur.next is None:   # checks for end of the list
                break
            cur.next = cur.next.next  
        cur = cur.next  # if at the end of list, this makes it so cur is None
    return head.next  # takes off the placeholder from the start

def pair(list1, list2):
    # no tail pointer but done recursivly so no O(n^2)
    if not list1 or not list2:  # if either list is over, finish our list 
        return None             # wtih a None and end recursion
    else:
        this_node = ListNode((list1.val, list2.val))  
        # gets the next node by calling this function with the next item 
        # in each list
        next_node = pair(list1.next, list2.next)    
        this_node.next = next_node
        return this_node

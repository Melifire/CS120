from list_node import ListNode

def array_to_list_recursive(data):
    # if there are any elements in the array
    if data:
        # created a list node with the current first value then sets its next value to 
        # the node returned by this function called on the list without the first index
        node = ListNode(data[0])
        child_node = array_to_list_recursive(data[1:])
        node.next = child_node
        return node
    else:
        # once there are no more items in the array, finish off the list with None
        return None

def accordion_recursive(head):
    # if the list has 0 or 1 element, return None
    if not head or not head.next:
        return None
    else:
        # if the list has no third element, then the second value is returned: base case
        if not head.next.next:
            return head.next
        else:
            # the method of calling recursion on the nodes that are going to be removed 
            # is used because the first node must always be removed and it is also 
            # always called
            in_three_nodes = head.next.next.next
            accordion_recursive(head.next.next)  # does not use the return value
            head = head.next
            head.next = in_three_nodes
            return head # return value is only used for calling from outside the function

def pair_recursive(head1, head2):
    #if either list is empty, we have reached the end and finish the list with None
    if head1 is None or head2 is None:
        return None
    else:
        # makes a list node and sets its value to a tup of the values of each lists heads
        node = ListNode((head1.val, head2.val))
        # sets its next node to the returned node of this function on the two lists 
        # without thier heads
        node.next = pair_recursive(head1.next, head2.next)
        return node
def is_sorted_recursive(head):
    # if there is no next value to compare then we have reached the end
    if not head or not head.next:
        return True
    # makes sure this node is in order with the next node then does the same 
    # for the next node till the end
    return head.val <= head.next.val and is_sorted_recursive(head.next)
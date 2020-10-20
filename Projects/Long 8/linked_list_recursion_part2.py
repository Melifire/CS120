from list_node import ListNode

def array_to_list_recursive(data):
    if data:
        node = ListNode(data[0])
        child_node = array_to_list_recursive(data[1:])
        node.next = child_node
        return node
    else:
        return None

def accordion_recursive(head):
    if not head or not head.next:
        return None
    else:
        if not head.next.next:
            return head.next
        else:
            in_three_nodes = head.next.next.next
            accordion_recursive(head.next.next)
            head = head.next
            head.next = in_three_nodes
            return head

def pair_recursive(head1, head2):
    if head1 is None or head2 is None:
        return None
    else:
        node = ListNode((head1.val, head2.val))
        node.next = pair_recursive(head1.next, head2.next)
        return node
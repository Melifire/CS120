def dl_remove(head, node):
    if node.next:
        node.next.prev = node.prev
    if node.prev:
        node.prev.next = node.next
    else:
        return head.next
    return head

def dl_insert_before(head, node, new_node):
    new_node.next = node
    if node.prev:
        node.prev.next = new_node
        new_node.prev = node.prev
    else:
        node.prev = new_node
        return new_node
    node.prev = new_node
    return head
    

def dl_insert_after(head, node, new_node):
    if node.next:
        node.next.prev = new_node
        new_node.next = node.next
    node.next = new_node
    new_node.prev = node
    return head

from list_node import ListNode
from graphics import graphics

def insert_node(list_head, node):
    if list_head is None:
        node.x = 50
        node.y = 75
        return node
    if node.val < list_head.val:
        node.next = list_head
        node.x = 50
        node.y = 75
        cur = list_head
        index = 1
        while cur:
            index += 1
            cur.x = 50 + index % 7 * 100
            cur.y = 75 + (index // 7) * 150
            cur = cur.next
        return node
    cur = list_head
    index = 0
    while cur.next is not None and cur.next.val < node.val:
        cur = cur.next
        index += 1
    node.next = cur.next
    cur.next = node
    cur = node
    cur.x = 50 + index % 7 * 100
    cur.y = 75 + (index // 7) * 150
    while cur:
        index += 1
        cur.x = 50 + index % 7 * 100
        cur.y = 75 + (index // 7) * 150
        cur = cur.next
    return list_head


def insert_animation(window, list_head, node):
    if list_head is None:
        return node
    if node.val < list_head.val:
        for frame in range(25):
            window.rectangle(node.x, node.y,
                             50, 50, '#888888')
            window.text(node.x + 25, node.y + 25, f'{node.val}')
            node.x += 10
            draw_list(window, list_head)
        node.next = list_head
        return node
    cur = list_head
    while cur.next is not None and cur.next.val < node.val:
        cur = cur.next
    node.next = cur.next
    cur.next = node
    return list_head




def draw_list(window, linked_list, update_frame = 0):
    window.clear()
    window.rectangle(0, 0, 800, 800, '#555555')
    cur = linked_list
    pos = 1
    while cur is not None:
        window.rectangle(cur.x, cur.y, 
                        50, 50, '#888888')
        window.text(cur.x + 25, cur.y + 25, f'{cur.val}')
        cur = cur.next
        pos += 1
    window.update_frame(24)

def insert_node_vis(window, old_linked_list, new_linked_list):
    pass

def main():
    nodes = [
        ListNode(5),
        ListNode(5),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(10),
        ListNode(5)

    ]


    linked_list = None
    for node in nodes:
        linked_list = insert_node(linked_list, node)

    print(linked_list)

    window_width = 800
    window_height = 800
    frames_per_second = 30

    window = graphics(window_width, window_height, 'main')

    draw_list(window, linked_list, None)
    input()

    new_node = ListNode(15)
    insert_animation(window, linked_list, new_node)

    input()



if __name__ == '__main__':
    main()

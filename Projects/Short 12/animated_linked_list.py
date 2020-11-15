import time
import sys
import random as rn
from list_node import ListNode
from graphics import graphics

def insert_node_without_animation(list_head, node):
    if list_head is None:
        node.x = 50
        node.y = 75
        print("After insertion, the list is now:", node)
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
        print("After insertion, the list is now:", node)
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
    print("After insertion, the list is now:", list_head)
    return list_head


def insert_node(window, list_head, node):
    for _ in range(15):
        node.x += 10
        draw_list(window, list_head, node)
    if list_head is None:
        for _ in range(10):
            node.y += 6.5
            draw_list(window, list_head, node)
        print("After insertion, the list is now:", node)
        draw_list(window, node)
        return node
    if node.val < list_head.val:
        for _ in range(10):
            increase_all_next_nodes(list_head, 10)
            draw_list(window, list_head, node)
        for _ in range(10):
            node.y += 6.5
            draw_list(window, list_head, node)
        node.next = list_head
        print("After insertion, the list is now:", node)
        draw_list(window, node)
        return node
    cur = list_head
    index = 1
    for _ in range(10):
        node.x += 10
        draw_list(window, list_head, node)
    while cur.next is not None and cur.next.val < node.val:
        for _ in range(10):
            if node.x == 700:
                node.x = 0
                node.y += 150
                index = 0
            node.x += 10
            draw_list(window, list_head, node)
        index += 1
        cur = cur.next
    for _ in range(10):
        increase_all_next_nodes(cur.next, 10)
        draw_list(window, list_head, node)
    for _ in range(10):
        node.y += 6.5
        draw_list(window, list_head, node)
    node.next = cur.next
    cur.next = node
    draw_list(window, list_head)
    print("After insertion, the list is now:", list_head)
    return list_head


def increase_all_next_nodes(head, amount):
    if head is None:
        return None
    head.x += amount
    if head.x == 700:
        head.x = 0
        head.y += 150
    increase_all_next_nodes(head.next, amount)


def draw_list(window, linked_list, node = None):
    window.clear
    window.canvas.delete('all')

    window.rectangle(0, 0, 800, 800, '#555555')
    cur = linked_list
    pos = 1
    while cur is not None:
        window.line(cur.x + 25, cur.y + 25, cur.x + 125, cur.y + 25)
        window.rectangle(cur.x, cur.y, 
                        50, 50, '#888888')
        
        window.text(cur.x + 25, cur.y + 25, f'{cur.val}')
        cur = cur.next
        pos += 1
    
    if node is not None:
        window.rectangle(node.x, node.y,
                         50, 50, '#888888')
        window.text(node.x + 25, node.y + 25, f'{node.val}')

    window.update_frame(24)

def main():
    '''
    nodes = [

        ListNode(13),
        ListNode(0),
        ListNode(15),
        ListNode(9),
        ListNode(20),
        ListNode(1),
        ListNode(100),
        ListNode(-2000),
        ListNode(6)

    ]
    '''

    window_width = 800
    window_height = 800
    window = graphics(window_width, window_height, 'main')

    '''
    linked_list = None
    for node in nodes:
        linked_list = insert_node(window, linked_list, node)
    '''

    linked_list = None
    for line in sys.stdin:
        if not line:
            continue
        for num in line.split():
            new_node = ListNode(int(num))
            linked_list = insert_node(window, linked_list, new_node)

    '''
    linked_list = None
    for _ in range(49):
        val = rn.randrange(-100, 100)
        new_node = ListNode(val)
        linked_list = insert_animation(window, linked_list, new_node)
    '''

if __name__ == '__main__':
    main()

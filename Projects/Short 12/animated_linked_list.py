import time
import sys
import random as rn
from list_node import ListNode
from graphics import graphics

def insert_node_without_animation(list_head, node):
    '''This method is mainly used for debugging or if you want to use the 
    graphical version of this program without waiting for the animation.'''
    if list_head is None:  # if the list hasnt been created, node is the head
        node.x = 50
        node.y = 75
        print("After insertion, the list is now:", node)
        return node
    if node.val < list_head.val:  
        node.next = list_head
        node.x = 50
        node.y = 75
        cur = list_head
        index = 1  # an index is used to make finding the x, y position easier
        while cur:
            index += 1
            cur.x = 50 + index % 7 * 100
            cur.y = 75 + (index // 7) * 150
            cur = cur.next
        print("After insertion, the list is now:", node)
        # if node is the first item in the new list, return that to be the head
        return node
    cur = list_head
    index = 0
    # loops through each value until the desired node is found
    while cur.next is not None and cur.next.val < node.val:
        cur = cur.next
        index += 1
    # then does the insert
    node.next = cur.next
    cur.next = node

    # this loop section reassigns the position of every node after the insert
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
    '''the standard insert node animation for this project'''
    # if not using the modified version of the list node class, use the 
    # nongraphical insert instead
    try:
        node.x is not None
    except AttributeError:
        return insert_node_old_list(list_head, node)

    # moves the new node into the starting position above the first node
    for _ in range(15):
        node.x += 10
        draw_list(window, list_head, node)
    # if there is no starting node, just drop the new one into place
    if list_head is None:
        for _ in range(10):
            node.y += 6.5
            draw_list(window, list_head, node)
        print("After insertion, the list is now:", node)
        draw_list(window, node)
        return node
    # if the new node is less than the old head, move all the nodes and 
    # put the new node down
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
    # loop moves the new node to above the second node
    for _ in range(10):
        node.x += 10
        draw_list(window, list_head, node)
    # this loop goes through the list untill the desired position is found
    while cur.next is not None and cur.next.val < node.val:
        # over 10 frames, moves the node to the next position
        for _ in range(10):
            if node.x == 700:
                node.x = 0
                node.y += 150
            node.x += 10
            draw_list(window, list_head, node)
        cur = cur.next
    # moves all following nodes to the next position
    for _ in range(10):
        increase_all_next_nodes(cur.next, 10)
        draw_list(window, list_head, node)
    # moves the new node down
    for _ in range(10):
        node.y += 6.5
        draw_list(window, list_head, node)
    node.next = cur.next
    cur.next = node
    draw_list(window, list_head)
    print("After insertion, the list is now:", list_head)
    return list_head

def insert_node_old_list(head, node):
    '''nongraphical version used for the auto grader and anytime the new 
    list_node class is not used'''
    if head is None:
        print("After insertion, the list is now:", node)
        return node
    if node.val < head.val:
        node.next = head
        print("After insertion, the list is now:", node)
        return node
    cur = head
    while cur.next is not None and node.val >= cur.next.val:
        cur = cur.next
    node.next = cur.next
    cur.next = node
    print("After insertion, the list is now:", head)
    return head

def increase_all_next_nodes(head, amount):
    '''recursivly goes through and increases the x of all following nodes by a 
    given value. also moves nodes to the next line when appropriate'''
    if head is None:
        return None
    head.x += amount
    # moves to the next line if needed
    if head.x == 700:
        head.x = 0
        head.y += 150
    increase_all_next_nodes(head.next, amount)


def draw_list(window, linked_list, node = None):
    window.clear
    # deletes all the old objects, without this the program slows significantly
    window.canvas.delete('all')

    # draws the background
    window.rectangle(0, 0, 800, 800, '#555555')

    # loops through the given list and draws all the elements
    cur = linked_list
    pos = 1
    while cur is not None:
        window.line(cur.x + 25, cur.y + 25, cur.x + 125, cur.y + 25)
        window.rectangle(cur.x, cur.y, 
                        50, 50, '#888888')
        
        window.text(cur.x + 25, cur.y + 25, f'{cur.val}')
        cur = cur.next
        pos += 1
    
    # if a lone node is also passed to the function, draw that as well
    # this is the new node as it is not yet in the linked list
    if node is not None:
        window.rectangle(node.x, node.y,
                         50, 50, '#888888')
        window.text(node.x + 25, node.y + 25, f'{node.val}')

    window.update_frame(24)

def main():

    window_width = 800
    window_height = 800
    window = graphics(window_width, window_height, 'main')

    '''
    # this commented block can be used to predefine some nodes to add
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

    linked_list = None
    for node in nodes:
        linked_list = insert_node(window, linked_list, node)
    '''

    linked_list = None
    for line in sys.stdin:
        if not line:
            continue
        if line.strip() == 'exit':  # exit is used to stop the loop
            break
        for num in line.split():
            new_node = ListNode(int(num))
            linked_list = insert_node(window, linked_list, new_node)

    '''
    # this commented block can be used to generate random nodes
    linked_list = None
    for _ in range(49):
        val = rn.randrange(-100, 100)
        new_node = ListNode(val)
        linked_list = insert_animation(window, linked_list, new_node)
    '''

if __name__ == '__main__':
    main()

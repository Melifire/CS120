import time
import sys
import random as rn
from tree_node import TreeNode
from graphics import graphics
   

def insert_node_nongraph(head, node):
    '''nongraphical version used for the auto grader and anytime the new 
    list_node class is not used'''
    if head is None:
        return node
    assert head.val is not node.val, 'This is not required'
    node.depth += 1
    if node.val < head.val:
        if head.left:
            insert_node_nongraph(head.left, node)
        else:
            head.left = node
    else:
        if head.right:
            insert_node_nongraph(head.right, node)
        else:
            head.right = node

    head.subtree_count += 1
    return head

def insert_node(head, node):
    if head is None:
        return node
    assert head.val is not node.val, f'{node.val} already in tree'
    node.depth += 1
    if node.val < head.val:
        if head.left:
            insert_node_nongraph(head.left, node)
        else:
            head.left = node
    else:
        if head.right:
            insert_node_nongraph(head.right, node)
        else:
            head.right = node

    head.subtree_count += 1
    return head
    

'''
def increase_all_next_nodes(head, amount):
    recursivly goes through and increases the x of all following nodes by a 
    given value. also moves nodes to the next line when appropriate
    if head is None:
        return None
    head.x += amount
    # moves to the next line if needed
    if head.x == 700:
        head.x = 0
        head.y += 150
    increase_all_next_nodes(head.next, amount)
'''


def draw_tree(window, head, width, left_bound, node = None):
    if head is None:
        return False

    node_count = head.subtree_count + 1
    if head.left:
        index = head.left.subtree_count + 1
    else:
        index = 1

    x = index/node_count * width

    window.rectangle(x+left_bound, 100 + head.depth * 100, 50, 50)
    window.text(x+left_bound, 100 + head.depth * 100, str(head.val), 'blue')



    left_node = draw_tree(window, head.left, x, left_bound)
    right_node = draw_tree(window, head.right, width-x, x+left_bound)
    if left_node:
        window.line(x+left_bound, 100 + head.depth * 100, left_node[0], left_node[1])
    if right_node:
        window.line(x+left_bound, 100 + head.depth * 100, *right_node)
    return (x+left_bound, 100 + head.depth * 100)


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

    bts = None
    for line in sys.stdin:
        if not line:
            continue
        if line.strip() == 'exit':  # exit is used to stop the loop
            break
        for num in line.split():
            new_node = TreeNode(int(num))
            bts = insert_node_nongraph(bts, new_node)

        window.clear
        window.canvas.delete('all')
        draw_tree(window, bts, window_width, 0)
        print(bts)
        window.update()

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

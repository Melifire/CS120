from list_node import ListNode


def list_to_array(head):
    '''recusivly adds the head node's value to a list then runs the function
    again with the next node. The fuction is not run again once it reaches its
    last node. This method follows from the recursive deffenition for a linked
    list.'''
    if not head:
        return []
    if head.next:
        return [head.val] + list_to_array(head.next)
    else:
        return [head.val]

def array_to_list(input_array):
    '''this fuction works recursivly by creating a node with the first value in
    the list, then setting its next node to the return value of this fuction 
    called again minus its first value. once there are no more values in the
    array, it returns None, finishing off the linked list and ending the 
    recursion'''
    if input_array:
        node = ListNode(input_array[0])
        node.next = array_to_list(input_array[1:])
        return node
    else:
        return None

def append_list_to_list(head_1, head_2):
    '''runs through the first list untill it finds the end, then sets the last
    nodes next pointer to the head of the second list'''
    #if there isnt a first list, then the second list is the full result
    if not head_1:
        return head_2
    #these lines set cur to the last value in the list
    cur = head_1
    while cur.next:
        cur = cur.next
    #sets the next pointer to the second list
    cur.next = head_2
    return head_1


def list_length(head):
    '''checks if theres a next node then, if so, returns 1 + the value of this 
    function called on the next node. if not, returns 0, ending the 
    recursion'''
    if head:
        return 1 + list_length(head.next)
    else:
        return 0


def split_list(head):
    '''calls this files list_length() function to determine the length, then
    cur loops through for half the length rounded up. once cur is where the 
    last node of the first list would be, I set a second pointer to its next 
    node, the head of the second list, then set curs next node to None.
    '''
    length = list_length(head)
    if length == 0:
        return (None, None)
    cur = head
    for _ in range(round(length/2+.1)-1):
        cur = cur.next
    head_2 = cur.next
    cur.next = None
    return(head, head_2)


def accordion(head):
    '''checks to see of the current node has a next node that isnt None. If so
    just set the current values next node to that of its child, 
    effectivly removing it from the list. if the next node is none than we 
    have reached the end and can return'''
    #off with its head (we start at the second node)
    if head is not None and head.next is not None:
        head = head.next
    else:
        return None
    
    cur = head
    while cur is not None and cur.next is not None:
        cur.next = cur.next.next
        cur = cur.next
    return head



def too_many_aliases():
    a = [11, 22]
    b = [33, 44]
    ab1 = [a, b]
    ab2 = [a, b]
    out = [ab1, ab2, ab1, ab2]
    return out


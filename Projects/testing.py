class Node():
    next = None
    value = None

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def print_list_2(self):
        print(self.value)
        if self.next:
            return 1 + self.next.print_list_2()
        else:
            return 1

    def printList(self):
        cur = self
        count = 0

        while cur:
            count += 1
            print(cur)
            cur = cur.next

        return count

    def addNode(self, newNode):
        newNode.next = self.next
        self.next = newNode

    
def print_back(head):
    if head is None: #base case
        return None
    else:
        print_back(head.next)
        print(head.value)

def remove_third__linked_list(old_list):
    index = 0
    cur = old_list
    while index < 1 and cur:
        cur = cur.next
        index += 1
    if cur and cur.next:
        cur.next = cur.next.next
    return old_list

def reverse_list(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    end = reverse_list(head.next)
    next_node.next = head
    head.next = None
    return end

nodes = [Node(1), Node(2), Node(3), Node(4)]
for node in range(len(nodes)-1):
    nodes[node].next = nodes[node+1]

link = nodes[0]

link.printList()
link = reverse_list(link)
link.printList()

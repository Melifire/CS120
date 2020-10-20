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



head = Node(-17)
n2 = Node(2)
n3 = Node(5)
n4 = Node(23)

head.next = n2
n2.next = n3
n3.next = n4

head.printList()
remove_third__linked_list(head)
print('----')
head.printList()

from list_insert import ListNode, sorted_list_insert, print_list

# checks the two assertions
try:
    node = ListNode(17)
except AssertionError:
    print("Assertion caught: Data type must be a tuple")

try:
    node = ListNode((17, 14, 28))
except AssertionError:
    print("Assertion caught: Tuple must have 2 elements")

# makes a new node
new_node = ListNode((10, 20))

# adds the new node to an empty head
head = None
print_list(head)

# prints the list to see an empty printed list
head = sorted_list_insert(head, new_node)

# adds a new node with a smaller second value to the head
new_node = ListNode((10, 15))
head = sorted_list_insert(head, new_node)

# adds a new node with a equal second value but smaller first value to the head
new_node = ListNode((5, 15))
head = sorted_list_insert(head, new_node)

# adds a node to the end of the linked list
new_node = ListNode((5, 30))
head = sorted_list_insert(head, new_node)

# inserts a node midway through the list
new_node = ListNode((10, 17))
head = sorted_list_insert(head, new_node)

# inserts a node based on the first value rather than the second
new_node = ListNode((1, 30))
head = sorted_list_insert(head, new_node)

# prints the list to show a printed list
print_list(head)

from tree_node import TreeNode

def tree_count(root):
    if root is None:
        return 0
    # counts this node as 1 then adds all the nodes on the left to all the nodes on the 
    # right
    return tree_count(root.left) + tree_count(root.right) + 1

def tree_sum(root):
    if root is None:
        return 0
    # returns this nodes value plus all the nodes on the left plus all the nodes on the 
    # right
    return tree_sum(root.left) + tree_sum(root.right) + root.val

def tree_depth(root):
    if root is None:
        return -1
    # because we are calling at the root, the depth of the root node must be the depth of
    # the tree and all the leaves must have a depth of 0. The depth of any node in 
    # between is 1 plus the maximum depth below it
    return max(tree_depth(root.left), tree_depth(root.right)) + 1

def tree_print(root):
    if root is None:
        pass
    else:
        # print the top node than do the same for each child
        print(root.val)
        tree_print(root.left)
        tree_print(root.right)

def tree_build_left_linked_list(data):
    if data:
        # similar to building a linked list just .next is replaced with .left. If there 
        # are any elements we create a node with the first value then set its child to 
        # the return of this fuction without the first value
        node = TreeNode(data[0])
        next_node = tree_build_left_linked_list(data[1:])
        node.left = next_node
        return node
    else:
        return None

def in_ord_rev(root):
    if root_ is None:
        pass
    in_ord_rev(root.right)
    print(root.val)
    in_ord_rev(root.left)



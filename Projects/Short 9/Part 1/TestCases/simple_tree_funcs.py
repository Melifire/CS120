from tree_node import TreeNode

def tree_count(root):
    if root is None:
        return 0
    return tree_count(root.left) + tree_count(root.right) + 1

def tree_sum(root):
    if root is None:
        return 0
    return tree_sum(root.left) + tree_sum(root.right) + root.val

def tree_depth(root):
    if root is None:
        return -1
    return max((tree_depth(root.left), tree_depth(root.right), -1)) + 1

def tree_print(root):
    if root is None:
        pass
    else:
        print(root.val)
        tree_print(root.left)
        tree_print(root.right)

def tree_build_left_linked_list(data):
    if data:
        node = TreeNode(data[0])
        next_node = tree_build_left_linked_list(data[1:])
        node.left = next_node
        return node
    else:
        return None

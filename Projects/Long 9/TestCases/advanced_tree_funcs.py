from tree_node import TreeNode

def bst_search_loop(root, val):
    while root is not None:
        if val > root.val:
            root = root.right
        elif val < root.val:
            root = root.left
        else: 
            return root
    return None
        
def tree_search(root, val):
    if root and root.val == val:
        return root
    elif root:
        return tree_search(root.left, val) or tree_search(root.right, val)
    else:
        return None

def bst_insert_loop(root, val):
    while root is not None:
        if val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
                return None
            root = root.right
        elif val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
                return None
            root = root.left
        else:
            print('Error: Value already in tree!') 
    print('Error: Loop finished without inserting value!')


def in_order_traversal_print(root):
    if root is None:
        pass
    else:
        in_order_traversal_print(root.left)
        print(root.val)
        in_order_traversal_print(root.right)


def pre_order_traversal_print(root):
    if root is None:
        pass
    else:
        print(root.val)
        pre_order_traversal_print(root.left)
        pre_order_traversal_print(root.right)


def post_order_traversal_print(root):
    if root is None:
        pass
    else:
        post_order_traversal_print(root.left)
        post_order_traversal_print(root.right)
        print(root.val)

def in_order_vals(root):
    if root is None:
        return []
    else:
        return in_order_vals(root.left) + \
                [root.val] + \
                in_order_vals(root.right)

def bst_max(root):
    if root is None:
        return -9223372036854775808
    else:
        return max((bst_max(root.left), bst_max(root.right), root.val))


def in_ord_rev(root):
    if root is None:
        return
    in_ord_rev(root.right)
    print(root.val)
    in_ord_rev(root.left)

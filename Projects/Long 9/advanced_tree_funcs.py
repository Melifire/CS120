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
                root.right = root
                return None
            root = root.right
        elif val < root.val:
            if root.left is None:
                root.left = root
                return None
            root = root.left
        print('Error: Value already in tree!') 
    print('Error: Loop finished without inserting value!')




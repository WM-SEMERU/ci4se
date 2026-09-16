def _is_bst(root, min_value=float('-inf'), max_value=float('inf')):
    if root is None:
        return True
    return min_value < root.value < max_value and _is_bst(root.left,
        min_value, root.value) and _is_bst(root.right, root.value, max_value)
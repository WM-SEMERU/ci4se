def avl_split_last(root):
    if root is None:
        raise IndexError('Empty tree has no maximum element')
    root, left, right = avl_release_kids(root)
    if right is None:
        new_root, last_node = left, root
    else:
        new_right, last_node = avl_split_last(right)
        new_root = avl_join(left, new_right, root)
    return new_root, last_node
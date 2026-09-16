def _get_tree_paths(tree, node_id, depth=0):
    if node_id == _tree.TREE_LEAF:
        raise ValueError('Invalid node_id %s' % _tree.TREE_LEAF)
    left_child = tree.children_left[node_id]
    right_child = tree.children_right[node_id]
    if left_child != _tree.TREE_LEAF:
        left_paths = _get_tree_paths(tree, left_child, depth=depth + 1)
        right_paths = _get_tree_paths(tree, right_child, depth=depth + 1)
        for path in left_paths:
            path.append(node_id)
        for path in right_paths:
            path.append(node_id)
        paths = left_paths + right_paths
    else:
        paths = [[node_id]]
    return paths
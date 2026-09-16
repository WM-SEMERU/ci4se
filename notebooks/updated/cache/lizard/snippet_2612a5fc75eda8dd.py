def _AddFieldPaths(node, prefix, field_mask):
    if not node:
        field_mask.paths.append(prefix)
        return
    for name in sorted(node):
        if prefix:
            child_path = prefix + '.' + name
        else:
            child_path = name
        _AddFieldPaths(node[name], child_path, field_mask)
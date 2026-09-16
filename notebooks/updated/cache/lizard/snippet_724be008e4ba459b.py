def visit_name(self, node, parent):
    context = self._get_context(node)
    if context == astroid.Del:
        newnode = nodes.DelName(node.id, node.lineno, node.col_offset, parent)
    elif context == astroid.Store:
        newnode = nodes.AssignName(node.id, node.lineno, node.col_offset,
            parent)
    elif node.id in CONST_NAME_TRANSFORMS:
        newnode = nodes.Const(CONST_NAME_TRANSFORMS[node.id], getattr(node,
            'lineno', None), getattr(node, 'col_offset', None), parent)
        return newnode
    else:
        newnode = nodes.Name(node.id, node.lineno, node.col_offset, parent)
    if context in (astroid.Del, astroid.Store):
        self._save_assignment(newnode)
    return newnode
def _get_node_name(self, node):
    res = getattr(node, 'name', None)
    if res is None:
        return res
    if isinstance(res, AST.TypeDecl):
        return res.declname
    return res
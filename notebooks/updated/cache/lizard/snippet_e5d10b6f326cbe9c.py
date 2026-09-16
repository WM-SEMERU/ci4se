def getRawIdent(self, node):
    if node is self:
        return node
    ident = getattr(node, 'graphident', None)
    return ident
def visit_tuple(self, node):
    if len(node.elts) == 1:
        return '(%s, )' % node.elts[0].accept(self)
    return '(%s)' % ', '.join(child.accept(self) for child in node.elts)
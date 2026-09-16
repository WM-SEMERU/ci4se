def visit_list(self, node):
    return '[%s]' % ', '.join(child.accept(self) for child in node.elts)
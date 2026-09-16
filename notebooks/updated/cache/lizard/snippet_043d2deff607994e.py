def visit_Set(self, node):
    if node.elts:
        elts_aliases = {ContainerOf(alias) for elt in node.elts for alias in
            self.visit(elt)}
    else:
        elts_aliases = None
    return self.add(node, elts_aliases)
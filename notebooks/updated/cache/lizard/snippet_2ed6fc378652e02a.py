def visit(self, node):
    f = self.get_visitor(node)
    if f is not None:
        return f(node)
    return self.generic_visit(node)
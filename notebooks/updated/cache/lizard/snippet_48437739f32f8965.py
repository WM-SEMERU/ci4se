def generic_visit(self, node):
    if node.__class__.__name__ == 'Name':
        if node.ctx.__class__ == ast.Load and node.id not in self.names:
            self.names.append(node.id)
    ast.NodeVisitor.generic_visit(self, node)
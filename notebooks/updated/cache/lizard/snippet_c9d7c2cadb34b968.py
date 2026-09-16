def visit_decorators(self, node, parent):
    newnode = nodes.Decorators(node.lineno, node.col_offset, parent)
    newnode.postinit([self.visit(child, newnode) for child in node.
        decorator_list])
    return newnode
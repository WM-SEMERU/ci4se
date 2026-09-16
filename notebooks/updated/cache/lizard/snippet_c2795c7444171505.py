def visit_subscript(self, node, parent):
    context = self._get_context(node)
    newnode = nodes.Subscript(ctx=context, lineno=node.lineno, col_offset=
        node.col_offset, parent=parent)
    newnode.postinit(self.visit(node.value, newnode), self.visit(node.slice,
        newnode))
    return newnode
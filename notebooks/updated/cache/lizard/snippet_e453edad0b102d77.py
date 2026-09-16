def visit_boolop(self, node, parent):
    newnode = nodes.BoolOp(self._bool_op_classes[type(node.op)], node.
        lineno, node.col_offset, parent)
    newnode.postinit([self.visit(child, newnode) for child in node.values])
    return newnode
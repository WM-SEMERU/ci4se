def visit_pass(self, node, parent):
    return nodes.Pass(node.lineno, node.col_offset, parent)
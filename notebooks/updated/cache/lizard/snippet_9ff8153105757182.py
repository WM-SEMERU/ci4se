def visit_simple_value_boolean_query(self, node):
    node.left, node.right = node.left.accept(self), node.right.accept(self)
    return node
def visit_List(self, node):
    self.generic_visit(node)
    if node.elts:
        for elt in node.elts:
            self.combine(node, elt, unary_op=self.builder.ListType)
    else:
        self.result[node] = self.builder.NamedType(
            'pythonic::types::empty_list')
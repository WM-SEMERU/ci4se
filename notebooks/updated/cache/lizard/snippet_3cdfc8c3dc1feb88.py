def visit_If(self, node):
    if node.find(nodes.Block) is not None:
        return self.generic_visit(node)
    try:
        val = self.visit(node.test).as_const()
    except nodes.Impossible:
        return self.generic_visit(node)
    if val:
        body = node.body
    else:
        body = node.else_
    result = []
    for node in body:
        result.extend(self.visit_list(node))
    return result
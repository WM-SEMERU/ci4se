def visit_ExceptHandler(self, node):
    if node.name:
        self.naming[node.name.id] = [frozenset()]
    for stmt in node.body:
        self.visit(stmt)
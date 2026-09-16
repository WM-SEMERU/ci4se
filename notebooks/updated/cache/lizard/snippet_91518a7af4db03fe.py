def visit_comprehension(self, node):
    return '%s%s' % ('async ' if node.is_async else '', super(
        AsStringVisitor3, self).visit_comprehension(node))
def visit_while(self, node):
    whiles = 'while %s:\n%s' % (node.test.accept(self), self._stmt_list(
        node.body))
    if node.orelse:
        whiles = '%s\nelse:\n%s' % (whiles, self._stmt_list(node.orelse))
    return whiles
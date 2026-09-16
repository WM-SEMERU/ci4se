def generic_visit(self, node):
    self._close_callable(node)
    super(_AstTreeScanner, self).generic_visit(node)
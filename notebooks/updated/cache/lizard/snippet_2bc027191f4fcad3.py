def eq(self, other):
    other_node = self.box(other).node
    return _expr(exprnode.eq(self.node, other_node))
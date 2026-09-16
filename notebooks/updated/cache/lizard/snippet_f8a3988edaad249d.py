def pushdown_not(self):
    node = self.node.pushdown_not()
    if node is self.node:
        return self
    else:
        return _expr(node)
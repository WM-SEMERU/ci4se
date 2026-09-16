def add_child(self, node):
    node._parent = self
    self._children.append(node)
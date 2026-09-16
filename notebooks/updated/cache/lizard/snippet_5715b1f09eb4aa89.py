def _add_node(self, node, depth):
    self._topmost_node.add_child(node, bool(depth[1]))
    self._stack.append((depth, node))
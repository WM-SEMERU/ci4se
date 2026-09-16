def node_as_tree(self, node, visitor=lambda self, node: self.
    _default_node_visitor(node), children=lambda self, node, visitor,
    children: self._default_node_children(node, visitor, children)):
    tree = visitor(self, node)
    tree.update(children(self, node, visitor, children))
    return tree
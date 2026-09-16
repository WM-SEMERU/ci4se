def get_leafs(self, name):
    r
    if self._validate_node_name(name):
        raise RuntimeError('Argument `name` is not valid')
    self._node_in_tree(name)
    return [node for node in self._get_subtree(name) if self.is_leaf(node)]
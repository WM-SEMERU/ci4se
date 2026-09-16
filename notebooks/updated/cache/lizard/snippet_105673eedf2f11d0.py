def get_node_parent(self, name):
    r
    if self._validate_node_name(name):
        raise RuntimeError('Argument `name` is not valid')
    self._node_in_tree(name)
    return self._db[self._db[name]['parent']] if not self.is_root(name) else {}
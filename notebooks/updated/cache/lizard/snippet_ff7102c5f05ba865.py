def _collapse_subtree(self, name, recursive=True):
    oname = name
    children = self._db[name]['children']
    data = self._db[name]['data']
    del_list = []
    while len(children) == 1 and not data:
        del_list.append(name)
        name = children[0]
        children = self._db[name]['children']
        data = self._db[name]['data']
    parent = self._db[oname]['parent']
    self._db[name]['parent'] = parent
    if parent:
        self._db[parent]['children'].remove(oname)
        self._db[parent]['children'] = sorted(self._db[parent]['children'] +
            [name])
    else:
        self._root = name
        self._root_hierarchy_length = len(self.root_name.split(self.
            _node_separator))
    for node in del_list:
        self._del_node(node)
    if recursive:
        for child in copy.copy(children):
            self._collapse_subtree(child)
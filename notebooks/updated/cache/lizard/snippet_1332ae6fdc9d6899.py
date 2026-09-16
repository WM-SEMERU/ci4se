def _get_node(self, treelist, pos):
    node = None
    if pos is not None:
        subtree = self._get_substructure(treelist, pos)
        if subtree is not None:
            node = subtree[0]
    return node
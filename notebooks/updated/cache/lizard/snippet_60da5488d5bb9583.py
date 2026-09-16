def distances_from_parent(self, leaves=True, internal=True, unlabeled=False):
    if not isinstance(leaves, bool):
        raise TypeError('leaves must be a bool')
    if not isinstance(internal, bool):
        raise TypeError('internal must be a bool')
    if not isinstance(unlabeled, bool):
        raise TypeError('unlabeled must be a bool')
    if leaves or internal:
        for node in self.traverse_preorder():
            if (leaves and node.is_leaf() or internal and not node.is_leaf()
                ) and (unlabeled or node.label is not None):
                if node.edge_length is None:
                    yield node, 0
                else:
                    yield node, node.edge_length
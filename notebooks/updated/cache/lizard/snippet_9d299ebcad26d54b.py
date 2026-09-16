def get_tree_root(self):
    root = self
    while root.up is not None:
        root = root.up
    return root
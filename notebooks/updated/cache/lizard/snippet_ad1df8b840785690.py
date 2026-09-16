def paths(self):
    paths = []
    for tree in self.components():
        paths += self._single_tree_paths(tree)
    return paths
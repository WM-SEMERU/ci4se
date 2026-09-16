def _fell_trees(self):
    if callable(self.fell_method):
        for tree in self.fell_method(list(self.trees)):
            self.trees.remove(tree)
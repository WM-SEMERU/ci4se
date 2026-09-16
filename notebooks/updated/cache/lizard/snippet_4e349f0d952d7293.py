def _internal_build(self):
    self.nodes = self.__tree.Nodes()
    self.edges = self.__tree.Edges()
    self.augmentedEdges = {}
    for key, val in self.__tree.AugmentedEdges().items():
        self.augmentedEdges[key] = list(val)
    self.root = self.__tree.Root()
    seen = set()
    self.branches = set()
    for e1, e2 in self.edges:
        if e1 not in seen:
            seen.add(e1)
        else:
            self.branches.add(e1)
        if e2 not in seen:
            seen.add(e2)
        else:
            self.branches.add(e2)
    self.leaves = set(self.nodes.keys()) - self.branches
    self.leaves.remove(self.root)
def add_edge(self, fro, to):
    self.add_node(fro)
    self.add_node(to)
    self.edges[fro].add(to)
def moralize(self):
    moral_graph = UndirectedGraph(self.to_undirected().edges())
    for node in self.nodes():
        moral_graph.add_edges_from(itertools.combinations(self.get_parents(
            node), 2))
    return moral_graph
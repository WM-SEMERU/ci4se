def subgraph(self, vertices):
    r
    adjacency = self.W[(vertices), :][:, (vertices)]
    try:
        coords = self.coords[vertices]
    except AttributeError:
        coords = None
    graph = Graph(adjacency, self.lap_type, coords, self.plotting)
    for name, signal in self.signals.items():
        graph.set_signal(signal[vertices], name)
    return graph
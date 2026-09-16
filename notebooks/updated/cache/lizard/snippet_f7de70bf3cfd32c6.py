def as_graph_queue(self, manifest, limit_to=None):
    if limit_to is None:
        graph_nodes = self.graph.nodes()
    else:
        graph_nodes = limit_to
    new_graph = _subset_graph(self.graph, graph_nodes)
    return GraphQueue(new_graph, manifest)
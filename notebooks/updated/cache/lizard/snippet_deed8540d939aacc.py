def predecessors(self, node, graph=None):
    if graph is None:
        graph = self.graph
    return [key for key in graph if node in graph[key]]
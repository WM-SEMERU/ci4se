def as_graph(self, depth=0):
    if depth in self._graph_cache:
        return self._graph_cache[depth]
    self._graph_cache[depth] = graph = Graph(self, depth=depth)
    return graph
def appendGraph(self, graph_name, graph):
    self._graphDict[graph_name] = graph
    self._graphNames.append(graph_name)
    if not self.isMultigraph and len(self._graphNames) > 1:
        raise AttributeError(
            'Simple Munin Plugins cannot have more than one graph.')
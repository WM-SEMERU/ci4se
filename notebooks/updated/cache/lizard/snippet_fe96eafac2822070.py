def getGraphFieldList(self, graph_name):
    graph = self._getGraph(graph_name, True)
    return graph.getFieldList()
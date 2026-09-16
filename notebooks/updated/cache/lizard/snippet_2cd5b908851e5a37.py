def get_dependants(self, run):
    if run in self._graph.nodes():
        return list(self._graph.successors(run))
    else:
        return []
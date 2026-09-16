def travel_to(self, dest, weight=None, graph=None):
    destn = dest.name if hasattr(dest, 'name') else dest
    if destn == self.location.name:
        raise ValueError("I'm already at {}".format(destn))
    graph = self.character if graph is None else graph
    path = nx.shortest_path(graph, self['location'], destn, weight)
    return self.follow_path(path, weight)
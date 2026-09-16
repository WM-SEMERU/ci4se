def clone(self):
    new_solution = self.__class__(self._problem, len(self._routes))
    for index, r in enumerate(self._routes):
        new_route = new_solution._routes[index]
        for node in r.nodes():
            new_node = new_solution._nodes[node]
            new_route.allocate([new_node])
    return new_solution
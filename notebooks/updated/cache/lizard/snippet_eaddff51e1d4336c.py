def add_edge(self, edge):
    u, v = edge
    both_exist = u in self.vertices and v in self.vertices
    if both_exist and self.components[u] is self.components[v]:
        raise InvariantError('Adding %r would form a cycle' % (edge,))
    if u == v:
        raise InvariantError('Cannot add loop: %r' % (edge,))
    self.add_vertex(u)
    self.add_vertex(v)
    self._vertices[u].add(v)
    self._vertices[v].add(u)
    smaller_component, bigger_component = self.sort_components(u, v)
    for vertex in smaller_component:
        bigger_component.add(vertex)
        self.components[vertex] = bigger_component
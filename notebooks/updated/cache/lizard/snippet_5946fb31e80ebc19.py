def add(self, name, graph):
    if name in self:
        raise ValueError('{0} exists in this GraphCollection'.format(name))
    elif hasattr(self, unicode(name)):
        raise ValueError('Name conflicts with an existing attribute')
    indexed_graph = self.index(name, graph)
    for s, t, attrs in indexed_graph.edges(data=True):
        attrs.update({'graph': name})
        self.master_graph.add_edge(s, t, **attrs)
    for n, attrs in indexed_graph.nodes(data=True):
        for k, v in attrs.iteritems():
            if k not in self.master_graph.node[n]:
                self.master_graph.node[n][k] = {}
            self.master_graph.node[n][k][name] = v
    dict.__setitem__(self, name, indexed_graph)
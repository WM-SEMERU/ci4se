def copy_from(self, g):
    renamed = {}
    for k, v in g.node.items():
        ok = k
        if k in self.place:
            n = 0
            while k in self.place:
                k = ok + (n,) if isinstance(ok, tuple) else (ok, n)
                n += 1
        renamed[ok] = k
        self.place[k] = v
    if type(g) is nx.MultiDiGraph:
        g = nx.DiGraph(g)
    elif type(g) is nx.MultiGraph:
        g = nx.Graph(g)
    if type(g) is nx.DiGraph:
        for u, v in g.edges:
            self.edge[renamed[u]][renamed[v]] = g.adj[u][v]
    else:
        assert type(g) is nx.Graph
        for u, v, d in g.edges.data():
            self.add_portal(renamed[u], renamed[v], symmetrical=True, **d)
    return self
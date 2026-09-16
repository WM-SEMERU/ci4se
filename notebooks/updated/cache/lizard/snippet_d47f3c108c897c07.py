def chk_edges(self):
    goids = set(self.go2obj)
    self.chk_edges_nodes(self.edges, goids, 'is_a')
    for reltype, edges in self.edges_rel.items():
        self.chk_edges_nodes(edges, goids, reltype)
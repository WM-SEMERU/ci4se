def contract_variables(self, u, v):
    adj = self.adj
    if u not in adj:
        raise ValueError('{} is not a variable in the binary quadratic model'
            .format(u))
    if v not in adj:
        raise ValueError('{} is not a variable in the binary quadratic model'
            .format(v))
    if v in adj[u]:
        if self.vartype is Vartype.BINARY:
            self.add_variable(u, adj[u][v])
        elif self.vartype is Vartype.SPIN:
            self.add_offset(adj[u][v])
        else:
            raise RuntimeError('unexpected vartype')
        self.remove_interaction(u, v)
    neighbors = list(adj[v])
    for w in neighbors:
        self.add_interaction(u, w, adj[v][w])
        self.remove_interaction(v, w)
    self.remove_variable(v)
def permute_graph(G, order):
    adj = G.matrix('dense')
    adj = adj[np.ix_(order, order)]
    return Graph.from_adj_matrix(adj)
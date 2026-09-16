def bipartite_vertex_cover(bigraph):
    V = range(len(bigraph))
    matchV = max_bipartite_matching(bigraph)
    matchU = [None for u in V]
    for v in V:
        if matchV[v] is not None:
            matchU[matchV[v]] = v
    visitU = [False for u in V]
    visitV = [False for v in V]
    for u in V:
        if matchU[u] is None:
            _alternate(u, bigraph, visitU, visitV, matchV)
    inverse = [(not b) for b in visitU]
    return inverse, visitV
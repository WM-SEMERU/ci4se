def mutual_information(corpus, featureset_name, min_weight=0.9, filter=lambda
    f, v, c, dc: True):
    graph = feature_cooccurrence(corpus, featureset_name, min_weight=1,
        filter=filter)
    mgraph = type(graph)()
    keep_nodes = set()
    fset = corpus.features[featureset_name]
    for s, t, attrs in graph.edges(data=True):
        p_ij = float(attrs['weight']) / len(corpus.papers)
        p_i = float(fset.documentCounts[fset.lookup[s]]) / len(corpus.papers)
        p_j = float(fset.documentCounts[fset.lookup[t]]) / len(corpus.papers)
        MI = _nPMI(p_ij, p_i, p_j)
        if MI >= min_weight:
            mgraph.add_edge(s, t, nPMI=MI, **attrs)
            keep_nodes.add(s)
            keep_nodes.add(t)
    for n in list(keep_nodes):
        mgraph.node[n].update(graph.node[n])
    return mgraph
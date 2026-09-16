def PMISc(S, method='JP'):
    S = remove_diagonal(S)
    weights, G, S, T = preprocess(S, coloring_method=method)
    return MIS(G, weights)
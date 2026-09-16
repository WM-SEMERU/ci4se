def connected_components(G):
    G = asgraph(G)
    N = G.shape[0]
    components = np.empty(N, G.indptr.dtype)
    fn = amg_core.connected_components
    fn(N, G.indptr, G.indices, components)
    return components
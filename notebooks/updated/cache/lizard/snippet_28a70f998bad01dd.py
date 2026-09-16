def extend_array(edges, binsz, lo, hi):
    numlo = int(np.ceil((edges[0] - lo) / binsz))
    numhi = int(np.ceil((hi - edges[-1]) / binsz))
    edges = copy.deepcopy(edges)
    if numlo > 0:
        edges_lo = np.linspace(edges[0] - numlo * binsz, edges[0], numlo + 1)
        edges = np.concatenate((edges_lo[:-1], edges))
    if numhi > 0:
        edges_hi = np.linspace(edges[-1], edges[-1] + numhi * binsz, numhi + 1)
        edges = np.concatenate((edges, edges_hi[1:]))
    return edges
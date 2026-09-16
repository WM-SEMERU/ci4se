def structural_imbalance(S, sampler=None, **sampler_args):
    h, J = structural_imbalance_ising(S)
    response = sampler.sample_ising(h, J, **sampler_args)
    sample = next(iter(response))
    colors = {v: ((spin + 1) // 2) for v, spin in iteritems(sample)}
    frustrated_edges = {}
    for u, v, data in S.edges(data=True):
        sign = data['sign']
        if sign > 0 and colors[u] != colors[v]:
            frustrated_edges[u, v] = data
        elif sign < 0 and colors[u] == colors[v]:
            frustrated_edges[u, v] = data
    return frustrated_edges, colors
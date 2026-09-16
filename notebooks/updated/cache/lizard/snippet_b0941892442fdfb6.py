def hamiltonian(edges, directed=False, precision=0):
    edges = populate_edge_weights(edges)
    incident, nodes = node_to_edge(edges, directed=False)
    DUMMY = 'DUMMY'
    dummy_edges = edges + [(DUMMY, x, 0) for x in nodes]
    if directed:
        dummy_edges += [(x, DUMMY, 0) for x in nodes]
        dummy_edges = reformulate_atsp_as_tsp(dummy_edges)
    tour = tsp(dummy_edges, precision=precision)
    dummy_index = tour.index(DUMMY)
    tour = tour[dummy_index:] + tour[:dummy_index]
    if directed:
        dummy_star_index = tour.index((DUMMY, '*'))
        assert dummy_star_index in (1, len(tour) - 1), tour
        if dummy_star_index == len(tour) - 1:
            tour = tour[1:] + tour[:1]
            tour = tour[::-1]
        path = tour[1:]
        path = [x for x in path if not isinstance(x, tuple)]
    else:
        path = tour[1:]
    return path
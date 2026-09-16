def markov_network(potentials):
    G = nx.Graph()
    G.name = 'markov_network({!r})'.format(potentials)
    for clique, phis in potentials.items():
        num_vars = len(clique)
        if not isinstance(phis, abc.Mapping):
            raise TypeError('phis should be a dict')
        elif not all(config in phis for config in itertools.product((0, 1),
            repeat=num_vars)):
            raise ValueError('not all potentials provided for {!r}'.format(
                clique))
        if num_vars == 1:
            u, = clique
            G.add_node(u, potential=phis)
        elif num_vars == 2:
            u, v = clique
            G.add_edge(u, v, potential=phis, order=(u, v))
        else:
            raise ValueError('Only supports cliques up to size 2')
    return G
def connections_from_graph(env, G, edge_data=False):
    if not issubclass(G.__class__, (Graph, DiGraph)):
        raise TypeError(
            "Graph structure must be derived from Networkx's Graph or DiGraph."
            )
    if not hasattr(env, 'get_agents'):
        raise TypeError("Parameter 'env' must have get_agents.")
    addrs = env.get_agents(addr=True)
    if len(addrs) != len(G):
        raise ValueError(
            'The number of graph nodes and agents in the environment (excluding the manager agent) must match. Now got {} nodes and {} agents.'
            .format(len(G), len(addrs)))
    addrs = sort_addrs(addrs)
    _addrs2nodes(addrs, G)
    conn_map = _edges2conns(G, edge_data)
    env.create_connections(conn_map)
def remove_isolated_nodes(graph):
    nodes = list(nx.isolates(graph))
    graph.remove_nodes_from(nodes)
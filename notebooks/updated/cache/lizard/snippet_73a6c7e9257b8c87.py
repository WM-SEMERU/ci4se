def generate_hypergraph(num_nodes, num_edges, r=0):
    random_graph = hypergraph()
    nodes = list(map(str, list(range(num_nodes))))
    random_graph.add_nodes(nodes)
    edges = list(map(str, list(range(num_nodes, num_nodes + num_edges))))
    random_graph.add_hyperedges(edges)
    if 0 == r:
        for e in edges:
            for n in nodes:
                if choice([True, False]):
                    random_graph.link(n, e)
    else:
        for e in edges:
            shuffle(nodes)
            for i in range(r):
                random_graph.link(nodes[i], e)
    return random_graph
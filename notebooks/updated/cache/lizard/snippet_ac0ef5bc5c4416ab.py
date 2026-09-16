def non_interactions(graph, t=None):
    nodes = set(graph)
    while nodes:
        u = nodes.pop()
        for v in (nodes - set(graph[u])):
            yield u, v
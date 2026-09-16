def write_cycle(filename, graph, cycle, directed):
    n = len(graph)
    weight = [([float('inf')] * n) for _ in range(n)]
    for r in range(1, len(cycle)):
        weight[cycle[r - 1]][cycle[r]] = r
        if not directed:
            weight[cycle[r]][cycle[r - 1]] = r
    write_graph(filename, graph, arc_label=weight, directed=directed)
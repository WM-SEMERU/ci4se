def truncateGraph(graph, root_nodes):
    subgraph = Graph()
    for node in root_nodes:
        subgraph = GraphUtils.joinGraphs(subgraph, GraphUtils.
            getReacheableSubgraph(graph, node))
    return subgraph
def get_irregular_edge_by_vertex(graph, vertex):
    for edge in graph.get_edges_by_vertex(vertex):
        if edge.is_irregular_edge:
            return edge
    return None
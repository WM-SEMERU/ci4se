def rcm_vertex_order(vertices_resources, nets):
    vertices_neighbours = _get_vertices_neighbours(nets)
    for subgraph_vertices in _get_connected_subgraphs(vertices_resources,
        vertices_neighbours):
        cm_order = _cuthill_mckee(subgraph_vertices, vertices_neighbours)
        for vertex in reversed(cm_order):
            yield vertex
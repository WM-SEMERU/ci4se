def remove_edge_fun(graph):
    rm_edge, rm_node = graph.remove_edge, graph.remove_node
    from networkx import is_isolate

    def remove_edge(u, v):
        rm_edge(u, v)
        if is_isolate(graph, v):
            rm_node(v)
    return remove_edge
def all_multi_paths(graph, source, target, data=False):
    r
    path_multiedges = list(nx_all_simple_edge_paths(graph, source, target,
        keys=True, data=data))
    return path_multiedges
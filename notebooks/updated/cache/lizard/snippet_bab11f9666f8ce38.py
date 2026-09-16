def _append_scc(graph, ordered_nodes, scc):
    loop_head = None
    for parent_node in reversed(ordered_nodes):
        for n in scc:
            if n in graph[parent_node]:
                loop_head = n
                break
        if loop_head is not None:
            break
    if loop_head is None:
        loop_head = next(iter(scc))
    subgraph = graph.subgraph(scc).copy()
    for src, _ in list(subgraph.in_edges(loop_head)):
        subgraph.remove_edge(src, loop_head)
    ordered_nodes.extend(CFGUtils.quasi_topological_sort_nodes(subgraph))
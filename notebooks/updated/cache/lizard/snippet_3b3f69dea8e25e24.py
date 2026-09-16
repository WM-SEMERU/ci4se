def cut_edges(graph):
    recursionlimit = getrecursionlimit()
    setrecursionlimit(max(len(graph.nodes()) * 2, recursionlimit))
    if 'hypergraph' == graph.__class__.__name__:
        return _cut_hyperedges(graph)
    pre = {}
    low = {}
    spanning_tree = {}
    reply = []
    pre[None] = 0
    for each in graph:
        if each not in pre:
            spanning_tree[each] = None
            _cut_dfs(graph, spanning_tree, pre, low, reply, each)
    setrecursionlimit(recursionlimit)
    return reply
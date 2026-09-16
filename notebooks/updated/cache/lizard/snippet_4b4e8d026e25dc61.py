def accessibility(graph):
    recursionlimit = getrecursionlimit()
    setrecursionlimit(max(len(graph.nodes()) * 2, recursionlimit))
    accessibility = {}
    for each in graph:
        access = {}
        _dfs(graph, access, 1, each)
        accessibility[each] = list(access.keys())
    setrecursionlimit(recursionlimit)
    return accessibility
def _elimination_trees(theta, decision_variables):
    auxiliary_variables = set(n for n in theta.linear if n not in
        decision_variables)
    adj = {v: {u for u in theta.adj[v] if u in auxiliary_variables} for v in
        theta.adj if v in auxiliary_variables}
    tw, order = dnx.treewidth_branch_and_bound(adj)
    ancestors = {}
    for n in order:
        ancestors[n] = set(adj[n])
        neighbors = adj[n]
        for u, v in itertools.combinations(neighbors, 2):
            adj[u].add(v)
            adj[v].add(u)
        for v in neighbors:
            adj[v].discard(n)
        del adj[n]
    roots = {}
    nodes = {v: {} for v in ancestors}
    for vidx in range(len(order) - 1, -1, -1):
        v = order[vidx]
        if ancestors[v]:
            for u in order[vidx + 1:]:
                if u in ancestors[v]:
                    nodes[u][v] = nodes[v]
                    break
        else:
            roots[v] = nodes[v]
    return roots, ancestors
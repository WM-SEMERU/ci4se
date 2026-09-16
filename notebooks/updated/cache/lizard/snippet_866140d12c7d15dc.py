def fill_traversals(traversals, edges, edges_hash=None):
    edges = np.asanyarray(edges, dtype=np.int64)
    edges.sort(axis=1)
    if len(traversals) == 0:
        return edges.copy()
    if edges_hash is None:
        edges_hash = grouping.hashable_rows(edges)
    splits = []
    for nodes in traversals:
        splits.extend(split_traversal(traversal=nodes, edges=edges,
            edges_hash=edges_hash))
    included = util.vstack_empty([np.column_stack((i[:-1], i[1:])) for i in
        splits])
    if len(included) > 0:
        included.sort(axis=1)
        splits.extend(grouping.boolean_rows(edges, included, operation=np.
            setdiff1d))
    else:
        splits = edges.copy()
    return splits
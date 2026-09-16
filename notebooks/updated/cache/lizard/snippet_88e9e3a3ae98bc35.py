def get_paths_to_simplify(G, strict=True):
    start_time = time.time()
    endpoints = set([node for node in G.nodes() if is_endpoint(G, node,
        strict=strict)])
    log('Identified {:,} edge endpoints in {:,.2f} seconds'.format(len(
        endpoints), time.time() - start_time))
    start_time = time.time()
    paths_to_simplify = []
    for node in endpoints:
        for successor in G.successors(node):
            if successor not in endpoints:
                try:
                    path = build_path(G, successor, endpoints, path=[node,
                        successor])
                    paths_to_simplify.append(path)
                except RuntimeError:
                    log('Recursion error: exceeded max depth, moving on to next endpoint successor'
                        , level=lg.WARNING)
    log('Constructed all paths to simplify in {:,.2f} seconds'.format(time.
        time() - start_time))
    return paths_to_simplify
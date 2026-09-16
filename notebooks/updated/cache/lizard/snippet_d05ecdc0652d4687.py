def truncate_graph_bbox(G, north, south, east, west, truncate_by_edge=False,
    retain_all=False):
    start_time = time.time()
    G = G.copy()
    nodes_outside_bbox = []
    for node, data in G.nodes(data=True):
        if data['y'] > north or data['y'] < south or data['x'] > east or data[
            'x'] < west:
            if not truncate_by_edge:
                nodes_outside_bbox.append(node)
            else:
                any_neighbors_in_bbox = False
                neighbors = list(G.successors(node)) + list(G.predecessors(
                    node))
                for neighbor in neighbors:
                    x = G.nodes[neighbor]['x']
                    y = G.nodes[neighbor]['y']
                    if y < north and y > south and x < east and x > west:
                        any_neighbors_in_bbox = True
                        break
                if not any_neighbors_in_bbox:
                    nodes_outside_bbox.append(node)
    G.remove_nodes_from(nodes_outside_bbox)
    log('Truncated graph by bounding box in {:,.2f} seconds'.format(time.
        time() - start_time))
    if not retain_all:
        G = remove_isolated_nodes(G)
        G = get_largest_component(G)
    return G
def graph_from_point(center_point, distance=1000, distance_type='bbox',
    network_type='all_private', simplify=True, retain_all=False,
    truncate_by_edge=False, name='unnamed', timeout=180, memory=None,
    max_query_area_size=50 * 1000 * 50 * 1000, clean_periphery=True,
    infrastructure='way["highway"]', custom_filter=None):
    if distance_type not in ['bbox', 'network']:
        raise InvalidDistanceType('distance_type must be "bbox" or "network"')
    north, south, east, west = bbox_from_point(center_point, distance)
    G = graph_from_bbox(north, south, east, west, network_type=network_type,
        simplify=simplify, retain_all=retain_all, truncate_by_edge=
        truncate_by_edge, name=name, timeout=timeout, memory=memory,
        max_query_area_size=max_query_area_size, clean_periphery=
        clean_periphery, infrastructure=infrastructure, custom_filter=
        custom_filter)
    if distance_type == 'network':
        centermost_node = get_nearest_node(G, center_point)
        G = truncate_graph_dist(G, centermost_node, max_distance=distance)
    log('graph_from_point() returning graph with {:,} nodes and {:,} edges'
        .format(len(list(G.nodes())), len(list(G.edges()))))
    return G
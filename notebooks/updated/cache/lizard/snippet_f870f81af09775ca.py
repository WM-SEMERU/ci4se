def connected_component_labels(edges, node_count=None):
    matrix = edges_to_coo(edges, node_count)
    body_count, labels = csgraph.connected_components(matrix, directed=False)
    assert len(labels) == node_count
    return labels
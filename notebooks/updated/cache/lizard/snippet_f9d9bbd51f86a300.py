def normalize_nodes(*nodes, headers=None):
    if not nodes:
        return normalize_node(DEFAULT_NODE, headers),
    normalized_nodes = ()
    for node in nodes:
        normalized_nodes += normalize_node(node, headers),
    return normalized_nodes
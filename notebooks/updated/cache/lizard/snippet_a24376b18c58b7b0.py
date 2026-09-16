def _edge_mapping(G):
    edge_mapping = {edge: idx for idx, edge in enumerate(G.edges)}
    edge_mapping.update({(e1, e0): idx for (e0, e1), idx in edge_mapping.
        items()})
    return edge_mapping
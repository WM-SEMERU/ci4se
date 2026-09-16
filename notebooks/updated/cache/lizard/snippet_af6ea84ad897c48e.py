def get_quadrant_from_class(node_class):
    up, edge_type, _ = node_class
    if up == 0:
        return 0 if random.random() < 0.5 else 7
    mappings = {(-1, 'modification'): 1, (-1, 'amount'): 2, (-1, 'activity'
        ): 3, (1, 'activity'): 4, (1, 'amount'): 5, (1, 'modification'): 6}
    return mappings[up, edge_type]
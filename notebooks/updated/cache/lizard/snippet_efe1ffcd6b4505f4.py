def get_distance(node1, node2):
    if node1 < 0 or node1 > get_max_node():
        raise ValueError(node1)
    if node2 < 0 or node2 > get_max_node():
        raise ValueError(node2)
    return libnuma.numa_distance(node1, node2)
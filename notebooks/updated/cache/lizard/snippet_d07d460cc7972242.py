def _find_longest_internal_edge(self, node):
    max_length = -1
    max_edge = None
    while node and not node.edge.rootedge:
        if node.edge.length > max_length:
            max_edge = node.edge
            max_length = max_edge.length
        node = node.parent_node
    return max_edge
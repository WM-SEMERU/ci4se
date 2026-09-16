def _get_connected_components_adjacency(self, graph, counts):
    found = set()
    components = list()
    for node in sorted(graph, key=lambda x: counts[x], reverse=True):
        if node not in found:
            component = breadth_first_search(node, graph)
            found.update(component)
            components.append(component)
    return components
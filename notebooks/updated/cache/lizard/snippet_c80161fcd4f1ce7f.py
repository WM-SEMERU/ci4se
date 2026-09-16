def search_nodes(self, **conditions):
    matching_nodes = []
    for n in self.iter_search_nodes(**conditions):
        matching_nodes.append(n)
    return matching_nodes
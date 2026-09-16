def add_hyperedges(self, hyperedges, attr_dict=None, **attr):
    attr_dict = self._combine_attribute_arguments(attr_dict, attr)
    hyperedge_ids = []
    for nodes in hyperedges:
        hyperedge_id = self.add_hyperedge(nodes, attr_dict.copy())
        hyperedge_ids.append(hyperedge_id)
    return hyperedge_ids
def alter_edge(self, from_index, to_index, to_jimage=None, new_weight=None,
    new_edge_properties=None):
    existing_edges = self.graph.get_edge_data(from_index, to_index)
    if not existing_edges:
        raise ValueError(
            'Edge between {} and {} cannot be altered;                                no edge exists between those sites.'
            .format(from_index, to_index))
    if to_jimage is None:
        edge_index = 0
    else:
        for i, properties in existing_edges.items():
            if properties['to_jimage'] == to_jimage:
                edge_index = i
    if new_weight is not None:
        self.graph[from_index][to_index][edge_index]['weight'] = new_weight
    if new_edge_properties is not None:
        for prop in list(new_edge_properties.keys()):
            self.graph[from_index][to_index][edge_index][prop
                ] = new_edge_properties[prop]
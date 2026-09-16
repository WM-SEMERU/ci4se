def build_unique_fragments(self):
    self.set_node_attributes()
    graph = self.graph.to_undirected()
    nm = iso.categorical_node_match('specie', 'ERROR')
    all_fragments = []
    for ii in range(1, len(self.molecule)):
        for combination in combinations(graph.nodes, ii):
            subgraph = nx.subgraph(graph, combination)
            if nx.is_connected(subgraph):
                all_fragments.append(subgraph)
    unique_fragments = []
    for fragment in all_fragments:
        if not [nx.is_isomorphic(fragment, f, node_match=nm) for f in
            unique_fragments].count(True) >= 1:
            unique_fragments.append(fragment)
    unique_mol_graphs = []
    for fragment in unique_fragments:
        mapping = {e: i for i, e in enumerate(sorted(fragment.nodes))}
        remapped = nx.relabel_nodes(fragment, mapping)
        species = nx.get_node_attributes(remapped, 'specie')
        coords = nx.get_node_attributes(remapped, 'coords')
        edges = {}
        for from_index, to_index, key in remapped.edges:
            edge_props = fragment.get_edge_data(from_index, to_index, key=key)
            edges[from_index, to_index] = edge_props
        unique_mol_graphs.append(self.with_edges(Molecule(species=species,
            coords=coords, charge=self.molecule.charge), edges))
    return unique_mol_graphs
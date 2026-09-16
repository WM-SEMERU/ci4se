def _construct_from_dataframe(self):
    direct_edges = {}
    feature_side_grouping = self.feature_pathway_df.groupby(['feature', 'side']
        )
    for (feature, _), group in feature_side_grouping:
        co_occurring_pathways = group['pathway'].tolist()
        pairings = list(itertools.combinations(co_occurring_pathways, 2))
        if not pairings:
            continue
        self.features.add(feature)
        for pathway0, pathway1 in pairings:
            vertex0_id = self.add_pathway(pathway0)
            vertex1_id = self.add_pathway(pathway1)
            new_edge = self.edge_tuple(vertex0_id, vertex1_id)
            if new_edge not in direct_edges:
                direct_edges[new_edge] = []
            direct_edges[new_edge].append(feature)
    self._augment_network(direct_edges)
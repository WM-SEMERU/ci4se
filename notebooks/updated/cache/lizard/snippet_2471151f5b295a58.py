def weight_by_edge_odds_ratios(self, edges_expected_weight, flag_as_significant
    ):
    for edge_id, expected_weight in edges_expected_weight:
        edge_obj = self.edges[edge_id]
        edge_obj.weight /= expected_weight
        if edge_id in flag_as_significant:
            edge_obj.significant = True
        else:
            edge_obj.significant = False
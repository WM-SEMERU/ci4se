def _check_hyperedge_id_consistency(self):
    hyperedge_ids_from_attributes = set(self._hyperedge_attributes.keys())
    forward_star_hyperedge_ids = set()
    for hyperedge_id_set in self._forward_star.values():
        forward_star_hyperedge_ids.update(hyperedge_id_set)
    backward_star_hyperedge_ids = set()
    for hyperedge_id_set in self._backward_star.values():
        backward_star_hyperedge_ids.update(hyperedge_id_set)
    if forward_star_hyperedge_ids != hyperedge_ids_from_attributes:
        raise ValueError('Consistency Check 4.1 Failed: hyperedge ids ' +
            'are different in the forward star ' +
            'values and the hyperedge ids from ' + 'attribute keys.')
    if backward_star_hyperedge_ids != hyperedge_ids_from_attributes:
        raise ValueError('Consistency Check 4.2 Failed: hyperedge ids ' +
            'are different in the backward star ' +
            'values and the hyperedge ids from ' + 'attribute keys.')
    predecessor_hyperedge_ids = set()
    for all_tails_from_predecessor in self._predecessors.values():
        for hyperedge_id in all_tails_from_predecessor.values():
            predecessor_hyperedge_ids.add(hyperedge_id)
    successor_hyperedge_ids = set()
    for all_heads_from_successor in self._successors.values():
        for hyperedge_id in all_heads_from_successor.values():
            successor_hyperedge_ids.add(hyperedge_id)
    if predecessor_hyperedge_ids != hyperedge_ids_from_attributes:
        raise ValueError('Consistency Check 4.3 Failed: hyperedge ids are ' +
            'different in the predecessor values and ' +
            'hyperedge ids from attribute keys.')
    if successor_hyperedge_ids != hyperedge_ids_from_attributes:
        raise ValueError('Consistency Check 4.4 Failed: hyperedge ids are ' +
            'different in the successor values and ' +
            'hyperedge ids from attribute keys.')
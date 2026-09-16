def rnni(self, use_weighted_choice=False, invert_weights=False):
    if use_weighted_choice:
        leaves = list(self.tree._tree.leaf_edge_iter())
        e, _ = self.tree.map_event_onto_tree(excluded_edges=leaves,
            invert_weights=invert_weights)
    else:
        e = random.choice(self.tree.get_inner_edges())
    children = self.get_children(e)
    h = random.choice(children['head'])
    t = random.choice(children['tail'])
    self.nni(e, h, t)
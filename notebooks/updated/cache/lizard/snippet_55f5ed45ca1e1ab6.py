def _precompute(self, tree):
    d = {}
    for n in tree.preorder_internal_node_iter():
        d[n] = namedtuple('NodeDist', ['dist_from_root', 'edges_from_root'])
        if n.parent_node:
            d[n].dist_from_root = d[n.parent_node
                ].dist_from_root + n.edge_length
            d[n].edges_from_root = d[n.parent_node].edges_from_root + 1
        else:
            d[n].dist_from_root = 0.0
            d[n].edges_from_root = 0
    return d
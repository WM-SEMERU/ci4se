def get_ring(self, tree_map, parent_map):
    assert parent_map[0] == -1
    rlst = self.find_share_ring(tree_map, parent_map, 0)
    assert len(rlst) == len(tree_map)
    ring_map = {}
    nslave = len(tree_map)
    for r in range(nslave):
        rprev = (r + nslave - 1) % nslave
        rnext = (r + 1) % nslave
        ring_map[rlst[r]] = rlst[rprev], rlst[rnext]
    return ring_map
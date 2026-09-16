def create_edges(self):
    s = self.idx_hierarchy.shape
    a = numpy.sort(self.idx_hierarchy.reshape(s[0], -1).T)
    a_unique, inv, cts = unique_rows(a)
    assert numpy.all(cts < 3
        ), 'No edge has more than 2 cells. Are cells listed twice?'
    self.is_boundary_edge = (cts[inv] == 1).reshape(s[1:])
    self.is_boundary_edge_individual = cts == 1
    self.edges = {'nodes': a_unique}
    self.cells['edges'] = inv.reshape(3, -1).T
    self._edges_cells = None
    self._edge_gid_to_edge_list = None
    self._edge_to_edge_gid = [[], numpy.where(self.
        is_boundary_edge_individual)[0], numpy.where(~self.
        is_boundary_edge_individual)[0]]
    return
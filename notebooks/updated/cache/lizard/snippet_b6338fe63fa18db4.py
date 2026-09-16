def add_self_edges(self, weight=None, copy=False):
    ii = np.arange(self.num_vertices())
    return self.add_edges(ii, ii, weight=weight, symmetric=False, copy=copy)
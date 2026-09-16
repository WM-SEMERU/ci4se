def get_axis_grid(self, ind):
    ng = self.dim
    num_pts = ng[ind]
    lengths = self.structure.lattice.abc
    return [(i / num_pts * lengths[ind]) for i in range(num_pts)]
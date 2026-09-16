def get_ir_reciprocal_mesh(self, mesh=(10, 10, 10), is_shift=(0, 0, 0)):
    shift = np.array([(1 if i else 0) for i in is_shift])
    mapping, grid = spglib.get_ir_reciprocal_mesh(np.array(mesh), self.
        _cell, is_shift=shift, symprec=self._symprec)
    results = []
    for i, count in zip(*np.unique(mapping, return_counts=True)):
        results.append(((grid[i] + shift * (0.5, 0.5, 0.5)) / mesh, count))
    return results
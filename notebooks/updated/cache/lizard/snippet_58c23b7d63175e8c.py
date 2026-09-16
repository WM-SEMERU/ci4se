def cell_centroids(self):
    if self._cell_centroids is None:
        self._cell_centroids = numpy.sum(self.node_coords[self.cells[
            'nodes']], axis=1) / 3.0
    return self._cell_centroids
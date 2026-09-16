def _coords2idx(self, coords):
    x = self._coords2vec(coords)
    idx = self._kd.query(x, p=self._metric_p, distance_upper_bound=self.
        _max_pix_scale)
    return idx[1]
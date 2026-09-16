def _edges_intersect(self, edge1, edge2):
    h12 = self._intersect_edge_arrays(self.pts[np.array(edge1)], self.pts[
        np.array(edge2)])
    h21 = self._intersect_edge_arrays(self.pts[np.array(edge2)], self.pts[
        np.array(edge1)])
    err = np.geterr()
    np.seterr(divide='ignore', invalid='ignore')
    try:
        out = 0 < h12 < 1 and 0 < h21 < 1
    finally:
        np.seterr(**err)
    return out
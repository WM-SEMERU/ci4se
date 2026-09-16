def get_distance_matrix(self):
    assert self.lons.ndim == 1
    distances = geodetic.geodetic_distance(self.lons.reshape(self.lons.
        shape + (1,)), self.lats.reshape(self.lats.shape + (1,)), self.lons,
        self.lats)
    return numpy.matrix(distances, copy=False)
def stations(self, *stns):
    self._set_query(self.spatial_query, stn=stns)
    return self
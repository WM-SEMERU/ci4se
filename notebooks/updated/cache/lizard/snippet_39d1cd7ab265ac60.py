def setup_local_geometry(self, isite, coords, optimization=None):
    self.local_geometry = AbstractGeometry(central_site=self.structure.
        cart_coords[isite], bare_coords=coords, centering_type=self.
        centering_type, include_central_site_in_centroid=self.
        include_central_site_in_centroid, optimization=optimization)
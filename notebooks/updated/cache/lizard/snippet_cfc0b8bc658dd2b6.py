def _load_modeling_extent(self):
    min_x, max_x, min_y, max_y = self.gssha_grid.bounds(as_projection=self.
        xd.lsm.projection)
    self._set_subset_indices(min_y, max_y, min_x, max_x)
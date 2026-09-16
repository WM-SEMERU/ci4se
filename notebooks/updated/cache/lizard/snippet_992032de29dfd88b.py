def projection_box(self, min_x, min_y, max_x, max_y):
    self._set_query(self.spatial_query, minx=min_x, miny=min_y, maxx=max_x,
        maxy=max_y)
    return self
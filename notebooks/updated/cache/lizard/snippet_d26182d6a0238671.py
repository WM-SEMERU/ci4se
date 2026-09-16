def point(self):
    if not self.geometry:
        raise ValueError(
            'geometry attribute must be set before trying to get point property'
            )
    if self.geometry.geom_type == 'Point':
        return self.geometry
    else:
        try:
            return self.geometry.point_on_surface
        except GEOSException:
            return self.geometry.centroid
def to_polygon(self, radius):
    assert radius > 0
    from openquake.hazardlib.geo.polygon import Polygon
    proj = geo_utils.OrthographicProjection(self.longitude, self.longitude,
        self.latitude, self.latitude)
    point = shapely.geometry.Point(*proj(self.longitude, self.latitude))
    return Polygon._from_2d(point.buffer(radius), proj)
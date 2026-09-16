def add_point(self, point):
    assert isinstance(point, GeoPoint), 'point should be GeoPoint instance'
    point_hash = self.get_point_hash(point)
    points = self.data.setdefault(point_hash, [])
    points.append(point)
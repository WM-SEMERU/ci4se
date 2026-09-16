def polygon(self):
    points = []
    for fp in self.points[1:]:
        points.append((fp.lat, fp.lng))
    return points
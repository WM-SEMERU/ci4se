def bounds(self, thr=0, lower_index=0, upper_index=-1):
    points = self.points[lower_index:upper_index]
    min_lat = float('inf')
    min_lon = float('inf')
    max_lat = -float('inf')
    max_lon = -float('inf')
    for point in points:
        min_lat = min(min_lat, point.lat)
        min_lon = min(min_lon, point.lon)
        max_lat = max(max_lat, point.lat)
        max_lon = max(max_lon, point.lon)
    return min_lat - thr, min_lon - thr, max_lat + thr, max_lon + thr
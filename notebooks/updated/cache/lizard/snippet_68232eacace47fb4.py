def distance(self, loc):
    assert type(loc) == type(self)
    lon1, lat1, lon2, lat2 = map(radians, [self.lon, self.lat, loc.lon, loc
        .lat])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371000
    return c * r
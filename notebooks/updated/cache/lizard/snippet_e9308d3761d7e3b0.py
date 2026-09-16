def project(self, lng_lat):
    lng, lat = lng_lat
    x = lng * DEG_TO_RAD
    lat = max(min(MAX_LATITUDE, lat), -MAX_LATITUDE)
    y = lat * DEG_TO_RAD
    y = log(tan(pi / 4 + y / 2))
    return x * EARTH_RADIUS, y * EARTH_RADIUS
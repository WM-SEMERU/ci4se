def for_point(cls, point, zoom):
    latitude, longitude = point.latitude_longitude
    return cls.for_latitude_longitude(latitude=latitude, longitude=
        longitude, zoom=zoom)
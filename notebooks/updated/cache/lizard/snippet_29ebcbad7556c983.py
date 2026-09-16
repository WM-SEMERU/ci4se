def _coerce_point_to_string(point, output_format='%(lat)s,%(lon)s'):
    try:
        if not isinstance(point, Point):
            point = Point(point)
    except ValueError as e:
        if isinstance(point, string_compare):
            warnings.warn(
                'Unable to parse the string as Point: "%s". Using the value as-is for the query. In geopy 2.0 this will become an exception.'
                 % str(e), DeprecationWarning, stacklevel=3)
            return point
        raise
    else:
        return output_format % dict(lat=point.latitude, lon=point.longitude)
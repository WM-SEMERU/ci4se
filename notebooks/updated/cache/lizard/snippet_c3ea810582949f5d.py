def normalize_lat_lng(arg):
    if isinstance(arg, dict):
        if 'lat' in arg and 'lng' in arg:
            return arg['lat'], arg['lng']
        if 'latitude' in arg and 'longitude' in arg:
            return arg['latitude'], arg['longitude']
    if _is_list(arg):
        return arg[0], arg[1]
    raise TypeError('Expected a lat/lng dict or tuple, but got %s' % type(
        arg).__name__)
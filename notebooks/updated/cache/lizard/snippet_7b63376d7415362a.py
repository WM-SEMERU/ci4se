def angular_distance(km, lat, lat2=None):
    if lat2 is not None:
        lat = max(abs(lat), abs(lat2))
    return km * KM_TO_DEGREES / math.cos(lat * DEGREES_TO_RAD)
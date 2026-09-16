def distance(latitude_1, longitude_1, elevation_1, latitude_2, longitude_2,
    elevation_2, haversine=None):
    if haversine or (abs(latitude_1 - latitude_2) > 0.2 or abs(longitude_1 -
        longitude_2) > 0.2):
        return haversine_distance(latitude_1, longitude_1, latitude_2,
            longitude_2)
    coef = math.cos(latitude_1 / 180.0 * math.pi)
    x = latitude_1 - latitude_2
    y = (longitude_1 - longitude_2) * coef
    distance_2d = math.sqrt(x * x + y * y) * ONE_DEGREE
    if (elevation_1 is None or elevation_2 is None or elevation_1 ==
        elevation_2):
        return distance_2d
    return math.sqrt(distance_2d ** 2 + (elevation_1 - elevation_2) ** 2)
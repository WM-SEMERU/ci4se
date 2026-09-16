def encode_polyline(features):
    points = list(read_points(features))
    latlon_points = [(x[1], x[0]) for x in points]
    return polyline.encode(latlon_points)
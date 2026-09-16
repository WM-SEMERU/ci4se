def polyline(*points):
    return Path(*[Line(points[i], points[i + 1]) for i in range(len(points) -
        1)])
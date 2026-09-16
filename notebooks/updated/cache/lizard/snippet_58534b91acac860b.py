def from_json(json):
    points = []
    for point in json['points']:
        points.append(Point.from_json(point))
    return Segment(points)
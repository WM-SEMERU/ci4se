def perpendicular_distance(p3, p1, p2):
    px = p2['x'] - p1['x']
    py = p2['y'] - p1['y']
    squared_distance = px * px + py * py
    if squared_distance == 0:
        line_point = Point(p1['x'], p1['y'])
        point = Point(p3['x'], p3['y'])
        return line_point.dist_to(point)
    u = ((p3['x'] - p1['x']) * px + (p3['y'] - p1['y']) * py
        ) / squared_distance
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    x = p1['x'] + u * px
    y = p1['y'] + u * py
    dx = x - p3['x']
    dy = y - p3['y']
    dist = math.sqrt(dx * dx + dy * dy)
    return dist
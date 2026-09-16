def polygon_diameter(points):
    return max(point_dist(p0, p1) for p0, p1 in combinations(points, 2))
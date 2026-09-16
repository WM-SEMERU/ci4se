def polygon_obb(polygon):
    if hasattr(polygon, 'exterior'):
        points = np.asanyarray(polygon.exterior.coords)
    elif isinstance(polygon, np.ndarray):
        points = polygon
    else:
        raise ValueError('polygon or points must be provided')
    return bounds.oriented_bounds_2D(points)
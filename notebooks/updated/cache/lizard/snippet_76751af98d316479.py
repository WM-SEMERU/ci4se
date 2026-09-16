def extrapolate_points(points, n_points):
    points = points[:n_points]
    lat = []
    lon = []
    last = None
    for point in points:
        if last is not None:
            lat.append(last.lat - point.lat)
            lon.append(last.lon - point.lon)
        last = point
    dts = np.mean([p.dt for p in points])
    lons = np.mean(lon)
    lats = np.mean(lat)
    gen_sample = []
    last = points[0]
    for _ in range(n_points):
        point = Point(last.lat + lats, last.lon + lons, None)
        point.dt = dts
        gen_sample.append(point)
        last = point
    return gen_sample
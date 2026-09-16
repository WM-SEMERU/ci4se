def kmeans(*args, **kwargs):
    lon, lat = _convert_measurements(args, kwargs.get('measurement', 'poles'))
    num = kwargs.get('num', 2)
    bidirectional = kwargs.get('bidirectional', True)
    tolerance = kwargs.get('tolerance', 1e-05)
    points = lon, lat
    dist = lambda x: stereonet_math.angular_distance(x, points, bidirectional)
    center_lon = np.random.choice(lon, num)
    center_lat = np.random.choice(lat, num)
    centers = np.column_stack([center_lon, center_lat])
    while True:
        dists = np.array([dist(item) for item in centers]).T
        closest = dists.argmin(axis=1)
        new_centers = []
        for i in range(num):
            mask = mask = closest == i
            _, vecs = cov_eig(lon[mask], lat[mask], bidirectional)
            new_centers.append(stereonet_math.cart2sph(*vecs[:, (-1)]))
        if np.allclose(centers, new_centers, atol=tolerance):
            break
        else:
            centers = new_centers
    return centers
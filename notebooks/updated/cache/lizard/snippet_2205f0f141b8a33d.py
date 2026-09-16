def kalman_filter(points, noise):
    kalman = ikalman.filter(noise)
    for point in points:
        kalman.update_velocity2d(point.lat, point.lon, point.dt)
        lat, lon = kalman.get_lat_long()
        point.lat = lat
        point.lon = lon
    return points
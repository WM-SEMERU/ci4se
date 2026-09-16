def propagate(p0, angle, d, deg=True, bearing=False, r=r_earth_mean):
    single, (p0, angle, d) = _to_arrays((p0, 2), (angle, 1), (d, 1))
    if deg:
        p0 = np.radians(p0)
        angle = np.radians(angle)
    if not bearing:
        angle = np.pi / 2.0 - angle
    lon0, lat0 = p0[:, (0)], p0[:, (1)]
    angd = d / r
    lat1 = arcsin(sin(lat0) * cos(angd) + cos(lat0) * sin(angd) * cos(angle))
    a = sin(angle) * sin(angd) * cos(lat0)
    b = cos(angd) - sin(lat0) * sin(lat1)
    lon1 = lon0 + arctan2(a, b)
    p1 = np.column_stack([lon1, lat1])
    if deg:
        p1 = np.degrees(p1)
    if single:
        p1 = p1[0]
    return p1
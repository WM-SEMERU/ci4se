def sphbear(lat1, lon1, lat2, lon2, tol=1e-15):
    ocross = lambda a, b: np.cross(a, b, axisa=0, axisb=0, axisc=0)
    v1 = np.asarray([np.cos(lat1) * np.cos(lon1), np.cos(lat1) * np.sin(
        lon1), np.sin(lat1)])
    v2 = np.asarray([np.cos(lat2) * np.cos(lon2), np.cos(lat2) * np.sin(
        lon2), np.sin(lat2)])
    is_bad = v1[0] ** 2 + v1[1] ** 2 < tol
    p12 = ocross(v1, v2)
    p1z = np.asarray([v1[1], -v1[0], np.zeros_like(lat1)])
    cm = np.sqrt((ocross(p12, p1z) ** 2).sum(axis=0))
    bearing = np.arctan2(cm, np.sum(p12 * p1z, axis=0))
    bearing = np.where(p12[2] < 0, -bearing, bearing)
    bearing = np.where(np.abs(bearing) < tol, 0, bearing)
    bearing[np.where(is_bad)] = np.nan
    return bearing
def subpoint(query_point, a=A, b=B):
    x, y, z = query_point
    lat = geodetic_lat(query_point)
    lon = np.arctan2(y, x)
    e2_ = (a * a - b * b) / (a * a)
    n__ = a / np.sqrt(1 - e2_ * np.sin(lat) ** 2)
    nx_ = n__ * np.cos(lat) * np.cos(lon)
    ny_ = n__ * np.cos(lat) * np.sin(lon)
    nz_ = (1 - e2_) * n__ * np.sin(lat)
    return np.stack([nx_, ny_, nz_], axis=0)
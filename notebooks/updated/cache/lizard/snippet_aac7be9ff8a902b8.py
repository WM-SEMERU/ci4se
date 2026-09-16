def ecef_to_geocentric(x, y, z, ref_height=None):
    if ref_height is None:
        ref_height = earth_geo_radius
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    colatitude = np.rad2deg(np.arccos(z / r))
    longitude = np.rad2deg(np.arctan2(y, x))
    latitude = 90.0 - colatitude
    return latitude, longitude, r - ref_height
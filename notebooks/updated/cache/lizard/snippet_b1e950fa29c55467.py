def stereonet2xyz(lon, lat):
    lon, lat = np.atleast_1d(lon, lat)
    x, y, z = sph2cart(lon, lat)
    return y, z, -x
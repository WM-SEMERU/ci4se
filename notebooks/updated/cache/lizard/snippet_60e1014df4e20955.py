def make_cos_vects(lon_vect, lat_vect):
    lon_rad = np.radians(lon_vect)
    lat_rad = np.radians(lat_vect)
    cvals = np.cos(lat_rad)
    xvals = cvals * np.sin(lon_rad)
    yvals = cvals * np.cos(lon_rad)
    zvals = np.sin(lat_rad)
    cvects = np.vstack([xvals, yvals, zvals])
    return cvects
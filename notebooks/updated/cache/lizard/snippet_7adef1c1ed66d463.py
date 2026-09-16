def angToPix(nside, lon, lat, nest=False):
    theta = np.radians(90.0 - lat)
    phi = np.radians(lon)
    return hp.ang2pix(nside, theta, phi, nest=nest)
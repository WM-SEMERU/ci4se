def dxyz2dlonlat(x, y, z, dfx, dfy, dfz):
    xs = np.array(x)
    ys = np.array(y)
    zs = np.array(z)
    lons = np.arctan2(ys, xs)
    lats = np.arcsin(zs)
    dfxs = np.array(dfx)
    dfys = np.array(dfy)
    dfzs = np.array(dfz)
    dlon = -dfxs * np.cos(lats) * np.sin(lons) + dfys * np.cos(lats) * np.cos(
        lons)
    dlat = -dfxs * np.sin(lats) * np.cos(lons) - dfys * np.sin(lats) * np.sin(
        lons) + dfzs * np.cos(lats)
    corr = np.sqrt(1.0 - zs ** 2)
    valid = ~np.isclose(corr, 0.0)
    dlon[valid] = dlon[valid] / corr[valid]
    return dlon, dlat
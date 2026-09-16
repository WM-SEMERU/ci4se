def mk_dx_dy_from_geotif_layer(geotif):
    ELLIPSOID_MAP = {'WGS84': 'WGS-84'}
    ellipsoid = ELLIPSOID_MAP[geotif.grid_coordinates.wkt]
    d = distance(ellipsoid=ellipsoid)
    dx = geotif.grid_coordinates.x_axis
    dy = geotif.grid_coordinates.y_axis
    dX = np.zeros(dy.shape[0] - 1)
    for j in xrange(len(dX)):
        dX[j] = d.measure((dy[j + 1], dx[1]), (dy[j + 1], dx[0])) * 1000
    dY = np.zeros(dy.shape[0] - 1)
    for i in xrange(len(dY)):
        dY[i] = d.measure((dy[i], 0), (dy[i + 1], 0)) * 1000
    return dX, dY
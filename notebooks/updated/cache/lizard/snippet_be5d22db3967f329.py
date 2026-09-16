def corners(bounds):
    bounds = np.asanyarray(bounds, dtype=np.float64)
    if util.is_shape(bounds, (2, 2)):
        bounds = np.column_stack((bounds, [0, 0]))
    elif not util.is_shape(bounds, (2, 3)):
        raise ValueError('bounds must be (2,2) or (2,3)!')
    minx, miny, minz, maxx, maxy, maxz = np.arange(6)
    corner_index = np.array([minx, miny, minz, maxx, miny, minz, maxx, maxy,
        minz, minx, maxy, minz, minx, miny, maxz, maxx, miny, maxz, maxx,
        maxy, maxz, minx, maxy, maxz]).reshape((-1, 3))
    corners = bounds.reshape(-1)[corner_index]
    return corners
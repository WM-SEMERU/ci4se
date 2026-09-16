def boxify_points(geom, rast):
    if 'Point' not in geom.type:
        raise ValueError('Points or multipoints only')
    buff = -0.01 * abs(min(rast.affine.a, rast.affine.e))
    if geom.type == 'Point':
        pts = [geom]
    elif geom.type == 'MultiPoint':
        pts = geom.geoms
    geoms = []
    for pt in pts:
        row, col = rast.index(pt.x, pt.y)
        win = (row, row + 1), (col, col + 1)
        geoms.append(box(*window_bounds(win, rast.affine)).buffer(buff))
    return MultiPolygon(geoms)
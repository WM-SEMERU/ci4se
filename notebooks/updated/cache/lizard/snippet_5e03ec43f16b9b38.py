def get_skydir_distance_mask(src_skydir, skydir, dist, min_dist=None,
    square=False, coordsys='CEL'):
    if dist is None:
        dist = 180.0
    if not square:
        dtheta = src_skydir.separation(skydir).rad
    elif coordsys == 'CEL':
        dtheta = get_linear_dist(skydir, src_skydir.ra.rad, src_skydir.dec.
            rad, coordsys=coordsys)
    elif coordsys == 'GAL':
        dtheta = get_linear_dist(skydir, src_skydir.galactic.l.rad,
            src_skydir.galactic.b.rad, coordsys=coordsys)
    else:
        raise Exception('Unrecognized coordinate system: %s' % coordsys)
    msk = dtheta < np.radians(dist)
    if min_dist is not None:
        msk &= dtheta > np.radians(min_dist)
    return msk